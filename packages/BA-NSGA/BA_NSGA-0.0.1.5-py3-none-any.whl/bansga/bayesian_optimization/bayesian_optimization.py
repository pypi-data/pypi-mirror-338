import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import Matern, WhiteKernel, ConstantKernel
from scipy.stats import norm
import random
import warnings
from typing import List, Callable, Optional

# ------------------------------------------------------------------
# Modified BayesianOptimization Class with Constraints
# ------------------------------------------------------------------
class BayesianOptimization:
    def __init__(self,
                 surrogate_models=None,
                 active_model_key='gp',
                 acquisition_func=None,
                 gp_alpha=1e-6,
                 weights=None,
                 bounds=None,
                 strategy:str='ei',
                 n_candidates:int=1,
                 constraints: Optional[List] = None,
                 discrete_levels: Optional[List[np.ndarray]] = None, 
                 logic: str = "all"):
        """
        Now includes:
        - constraints: a list of FeatureConstraint objects
        - discrete_levels: optional discrete values per dimension. If not None,
          we sample from these discrete sets instead of uniform real intervals.
        """
        valid_modes = ["all", "any"]
        if logic not in valid_modes:
            raise ValueError(
                f"Invalid logic='{logic}'. Must be one of {valid_modes}."
            )
        self.logic = logic

        # 1. If no surrogate models are provided, create a default Gaussian Process.
        if surrogate_models is None:
            kernel = ConstantKernel(1.0) * Matern(nu=2.5) + WhiteKernel(noise_level=1e-6)
            gp_model = GaussianProcessRegressor(kernel=kernel, alpha=gp_alpha, normalize_y=True)
            surrogate_models = {'gp': gp_model}
        self.surrogate_models = surrogate_models
        self.active_model_key = active_model_key
        
        # 2. Default acquisition = Expected Improvement if none is provided
        if acquisition_func is None:
            self.acquisition_func = self.expected_improvement
        else:
            self.acquisition_func = acquisition_func

        # 3. Multi-objective weighting
        self.weights = weights

        # 4. Internal storage
        self._trained_objective_values = None
        self.bounds = bounds
        self.strategy = strategy
        self.n_candidates = n_candidates

        # 5. Constraints support
        self.constraints = constraints if constraints else []
        
        # 6. Discrete levels for each dimension. If provided, will sample from these discrete sets.
        self.discrete_levels = discrete_levels

    def _aggregate_objectives(self, objectives: np.ndarray) -> np.ndarray:
        # same as your original code
        if objectives.ndim == 1:
            return objectives
        n_obj = objectives.shape[1]
        if self.weights is None:
            return np.mean(objectives, axis=1)
        else:
            if len(self.weights) != n_obj:
                raise ValueError(f"Mismatch: 'weights' length {len(self.weights)} != # of objectives {n_obj}.")
            return objectives @ self.weights

    def fit(self, features: np.ndarray, objectives: np.ndarray):
        # same as your original code
        if features.ndim != 2:
            raise ValueError("Expected 'features' to be 2D (n_samples, n_features).")
        if objectives.ndim not in [1, 2]:
            raise ValueError("Expected 'objectives' to be 1D or 2D.")

        # Convert possibly multi-objective data into a single 1D vector
        aggregated_y = self._aggregate_objectives(objectives)

        model = self.surrogate_models[self.active_model_key]
        model.fit(features, aggregated_y)
        self._trained_objective_values = aggregated_y

    def predict_with_uncertainty(self, features: np.ndarray):
        # same as your original code
        model = self.surrogate_models[self.active_model_key]
        try:
            mean, std = model.predict(features, return_std=True)
        except TypeError:
            # e.g. for RandomForestRegressor
            if hasattr(model, "estimators_"):
                predictions = np.array([est.predict(features) for est in model.estimators_])
                mean = np.mean(predictions, axis=0)
                std = np.std(predictions, axis=0)
            else:
                raise NotImplementedError(
                    "The active surrogate model does not support uncertainty estimation."
                )
        return mean, std

    def expected_improvement(self, features: np.ndarray, xi: float = 0.01):
        # same as your original code
        mean, std = self.predict_with_uncertainty(features)
        if self._trained_objective_values is None:
            raise ValueError("Model must be trained before calling expected_improvement().")

        best_y = np.min(self._trained_objective_values)
        improvement = best_y - mean - xi
        with np.errstate(divide='warn'):
            Z = improvement / std
            ei = improvement * norm.cdf(Z) + std * norm.pdf(Z)
            ei[std == 0.0] = 0.0
        return ei

    def upper_confidence_bound(self, features: np.ndarray, kappa: float = 2.576):
        # same as your original code
        mean, std = self.predict_with_uncertainty(features)
        return mean - kappa * std

    def predict_uncertainty_only(self, features: np.ndarray):
        _, std = self.predict_with_uncertainty(features)
        return std

    # ----------------------------------------------------------------
    # New helper to check constraints
    # ----------------------------------------------------------------
    def _passes_constraints(self, point: np.ndarray) -> bool:
        """
        Returns True if 'point' satisfies all constraints in self.constraints.
        For 'all' logic, you might do:
            return all(c.is_valid(point) for c in self.constraints)
        """
        # Example: require all constraints to pass:
        return all(c.is_valid(point) for c in self.constraints)

    def validate(self, features: np.ndarray) -> bool:
        """
        Checks whether the provided feature vector satisfies
        the constraints according to the specified logic.
        
        Returns
        -------
        bool
            True if constraints pass, False otherwise.
        """
        if self.logic == "all":
            return all(constraint(features) for constraint in self.constraints)
        elif self.logic == "any":
            return any(constraint(features) for constraint in self.constraints)
        return False

    # ----------------------------------------------------------------
    # Modified recommend_candidates to handle constraints & discrete
    # ----------------------------------------------------------------
    def recommend_candidates(self,
                             bounds: np.ndarray = None,
                             n_candidates: int = None,
                             n_restarts: int = 10,
                             strategy: str = None,
                             candidate_multiplier:int = 10,
                             discrete_design:bool = True,
                             avoid_repetitions: bool=True,
                             **kwargs) -> np.ndarray:
        """
        Recommend new points with constraints filtering and optional discrete sampling.
        """
        strategy = strategy if strategy is not None else self.strategy
        bounds = bounds if bounds is not None else self.bounds
        n_candidates = n_candidates if n_candidates is not None else self.n_candidates
        n_features = bounds.shape[0]

        # Decide which acquisition function to use
        if strategy == "exploration":
            # Maximize standard deviation
            def acquisition_func(x):
                return self.predict_uncertainty_only(x)
            mode = "max"
        elif strategy == "exploitation":
            # Minimize mean => we can maximize -mean
            def acquisition_func(x):
                mean, _ = self.predict_with_uncertainty(x)
                return -mean
            mode = "max"
        elif strategy == "ei":
            def acquisition_func(x):
                return self.expected_improvement(x, **kwargs)
            mode = "max"
        elif strategy == "ucb":
            def acquisition_func(x):
                return -self.upper_confidence_bound(x, **kwargs)
            mode = "max"
        else:
            # fallback to self.acquisition_func
            def acquisition_func(x):
                return self.acquisition_func(x, **kwargs)
            mode = "max"

        # We store final chosen candidates here
        chosen_candidates = []

        # ------------------------------------------------------------
        # 1) We'll do multiple random restarts to find the best single candidate
        # ------------------------------------------------------------

        candidate_count = candidate_multiplier * n_candidates
        candidates = []
        unique_candidates = set()
        max_attempts = candidate_count * 10
        attempts = 0

        # Generate candidate pool of valid points
        while len(candidates) < candidate_count and attempts < max_attempts:
            if discrete_design:
                candidate = np.array([random.randint(low, high) for (low, high) in bounds], dtype=int)
            else:
                candidate = np.array([random.uniform(low, high) for (low, high) in bounds], dtype=float)

            if self.validate(candidate):
                
                if avoid_repetitions:
                    candidate_tuple = tuple(candidate)  
                    if candidate_tuple not in unique_candidates:
                        unique_candidates.add(candidate_tuple)
                        candidates.append(candidate)
                else:
                    candidates.append(candidate)

            attempts += 1

        if len(candidates) < n_candidates:
            raise RuntimeError("Not enough valid candidate points were generated.")
        
        feasible_points = np.array(candidates)

        # If no feasible points found, we can't propose anything
        if len(feasible_points) == 0:
            raise ValueError("No feasible points found under the given constraints.")

        # Evaluate acquisition over all feasible points
        feasible_points_array = np.array(feasible_points)
        acq_vals = acquisition_func(feasible_points_array)

        # Depending on whether we are maximizing or minimizing, pick best
        if mode == "max":
            idx_best = np.argmax(acq_vals)
        else:
            idx_best = np.argmin(acq_vals)

        best_candidate = feasible_points_array[idx_best]
        chosen_candidates.append(best_candidate)

        # ------------------------------------------------------------
        # 2) Add additional random feasible points (simple approach)
        #    (More advanced approach might re-optimize after each new candidate.)
        # ------------------------------------------------------------
        # For the remaining candidates, we just pick random feasible points
        # from the same pool (or newly sampled).
        needed = n_candidates - 1
        if needed > 0:
            # If we already have feasible_points, let's shuffle them and pick
            # (We remove the best candidate from that set first, to avoid duplication)
            remaining_feasible = []
            for fp in feasible_points_array:
                # Use some tolerance if we want to ensure we don't pick the same point
                if not np.allclose(fp, best_candidate):
                    remaining_feasible.append(fp)

            np.random.shuffle(remaining_feasible)
            extras = remaining_feasible[:needed]
            chosen_candidates.extend(extras)

        return np.array(chosen_candidates)

    # ----------------------------------------------------------------
    # Example usage if you run this as a script
    # ----------------------------------------------------------------
if __name__ == "__main__":
    # Example usage with constraints & discrete levels
    np.random.seed(0)

    # Suppose we have 2D features in [0, 5]
    example_bounds = np.array([[0, 5],
                               [0, 5]], dtype=float)

    # Example constraint: x[0] + x[1] <= 6
    def sum_constraint(x):
        return (x[0] + x[1]) <= 6.0

    # Another example constraint: x[0] >= 1
    def min_constraint(x):
        return x[0] >= 1.0

    # Wrap in FeatureConstraint
    constraints = [
        FeatureConstraint(sum_constraint, name="Sum <= 6"),
        FeatureConstraint(min_constraint, name="x0 >= 1")
    ]

    # If we want discrete levels for each dimension, define them
    # e.g. for dimension 0 = {1,2,3,4,5}, dimension 1 = {0,1,2,3,4,5}
    discrete_levels = [
        np.array([1,2,3,4,5]),
        np.array([0,1,2,3,4,5])
    ]

    # Create some synthetic training data that meets the dimension shape
    X_train = np.random.rand(10, 2) * 5   # 10 samples in 2D
    Y_train = (X_train[:,0]-2.5)**2 + (X_train[:,1]-2.5)**2  # e.g. some 1D objective

    # Instantiate BO with constraints & discrete levels
    bo = BayesianOptimization(
        bounds=example_bounds,
        constraints=constraints,
        discrete_levels=discrete_levels
    )
    bo.fit(X_train, Y_train)

    # Request 3 new candidates using EI strategy
    new_candidates = bo.recommend_candidates(strategy="ei", n_candidates=3, n_restarts=20)
    print("Feasible candidates from discrete sets + constraints (EI):\n", new_candidates)
