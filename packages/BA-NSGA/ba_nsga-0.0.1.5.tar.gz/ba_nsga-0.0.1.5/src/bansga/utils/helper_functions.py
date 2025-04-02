"""
helper_functions.py
-------------------

Provides various helpers for checking convergence, generating random factors,
and other related tasks.
"""

import numpy as np
from sklearn.linear_model import Ridge
from scipy.optimize import lsq_linear

def solver_integer_local(X: np.ndarray, y: np.ndarray, regularization: float = 0.01, max_iter: int = 1000) -> np.ndarray:
    """
    Solves the regularized least squares problem with non-negative integer coefficients
    using a continuous relaxation followed by a simple local search (hill climbing).
    
    The optimization problem is defined as:
        minimize   || (X.T @ X + regularization * I) c - X.T @ y ||^2
        subject to c >= 0 and c is an integer vector.
    
    This method first computes a continuous solution using lsq_linear, rounds it to obtain an initial
    integer solution, and then iteratively improves it by checking local perturbations of each coefficient.
    
    Parameters
    ----------
    X : np.ndarray
        Design matrix with dimensions (n_samples, n_features).
    y : np.ndarray
        Response vector with dimensions (n_samples,).
    regularization : float, optional
        Regularization parameter (default is 0.01).
    max_iter : int, optional
        Maximum number of iterations for the local search (default is 1000).
    
    Returns
    -------
    np.ndarray
        Array of integer coefficients resulting from the optimization.
    """
    n_features = X.shape[1]
    
    # Construct matrix A and vector b for the formulation:
    # A = X.T @ X + regularization * I, and b = X.T @ y.
    A = X.T @ X + regularization * np.eye(n_features)
    b = X.T @ y

    # Define the objective function: f(c) = ||A*c - b||^2.
    def objective(c):
        return np.linalg.norm(A @ c - b)**2

    # Solve the continuous relaxation using lsq_linear.
    cont_sol = lsq_linear(A, b, bounds=(0, np.inf)).x
    
    # Round the continuous solution to obtain an initial integer solution.
    c_int = np.round(cont_sol).astype(int)
    # Ensure non-negative values.
    c_int = np.maximum(c_int, 0)
    
    current_value = objective(c_int)
    improved = True
    iterations = 0
    
    # Perform a simple local search (hill climbing).
    while improved and iterations < max_iter:
        improved = False
        for i in range(n_features):
            # Try adjusting the i-th coefficient by -1 and +1.
            for delta in [-1, 1]:
                candidate = c_int.copy()
                candidate[i] += delta
                # Skip if candidate becomes negative.
                if candidate[i] < 0:
                    continue
                candidate_value = objective(candidate)
                # If the candidate improves the objective, accept it.
                if candidate_value < current_value:
                    c_int = candidate
                    current_value = candidate_value
                    improved = True
                    break  # Exit inner loop if improvement is found.
            if improved:
                break  # Restart search from the new solution.
        iterations += 1

    return c_int

def oscillation_factor(generation, period, amplitude=1.0):
    """
    Computes an oscillation factor for the current generation using a cosine-based cycle.

    Parameters
    ----------
    generation : int
        Current generation index.
    period : int
        Number of generations per oscillation cycle.
    amplitude : float, optional
        Maximum amplitude of the oscillation. By default 1.0.

    Returns
    -------
    float
        A cyclical factor that varies between 0 and `amplitude * 2`.
        Example formula: amplitude * (1 + cos(2π * generation / period)).
    """
    return amplitude * (1.0 + np.cos(2.0 * np.pi * generation / period))

def decay_factor(generation, decay_rate):
    """
    Calculates an exponential decay factor from 1 down to near 0.

    Parameters
    ----------
    generation : int
        Current generation index.
    decay_rate : float
        Decay rate constant. Higher -> faster decay.

    Returns
    -------
    float
        Decay factor e^(-decay_rate * generation).
    """
    return np.exp(-decay_rate * generation)

def fitness_factor(objectives, weights=None, temperature=1.0, inflection_point=0.5, max_fitness=1.0):
    """
    Calculates a per-structure fitness factor from a multi-objective array.

    Parameters
    ----------
    self : object
        Must contain:
            - self.weights : array-like or None
                Weights for each objective. If None, equal weights are assumed.
            - self.temperature : float
                Temperature-like parameter for the logistic transform.
            - self.inflection_point : float (optional)
                Where the logistic midpoint is placed.
            - self.max_fitness : float (optional)
                A cap on the final logistic-based fitness.

    objectives : np.ndarray
        2D array of shape (N, K). Each row corresponds to a structure,
        each column is an objective. "Lower is better" is assumed.

    Returns
    -------
    np.ndarray
        1D array of shape (N,) giving the final fitness factor in [0..1].
        Larger => more favorable.
    """
    # Retrieve parameters with defaults
    N, K = objectives.shape

    # 1) Determine weights
    if weights is None:
        w = np.ones(K) / K
    else:
        w = np.array(weights, dtype=float)
        if w.shape[0] != K:
            raise ValueError("Length of self.weights must match # of objectives (K).")

    # 2) Min-max normalize each objective to 0..1 => 0 is best, 1 is worst
    eps = 1e-12
    norm_obj = np.zeros_like(objectives)
    for j in range(K):
        col = objectives[:, j]
        cmin, cmax = col.min(), col.max()
        spread = cmax - cmin
        if spread < eps:
            norm_obj[:, j] = 0.0
        else:
            norm_obj[:, j] = (col - cmin) / (spread + eps)

    # 3) Weighted sum => cost in [0..1]
    cost = np.dot(norm_obj, w)  # shape (N,)

    # 4) Convert cost -> logistic scale => 0..1
    #    If cost is lower, logistic => smaller => we might invert it.
    scaled = (cost - inflection_point) / (temperature + eps)
    logistic_values = 1.0 / (1.0 + np.exp(scaled))

    # 5) Cap them if desired
    logistic_values = np.minimum(logistic_values, max_fitness)

    # 6) Invert so that 1 => "best", 0 => "worst"
    #    i.e. cost=0 => logistic ~ a bit > 0 => fitness => close to 1
    fitness = 1.0 - logistic_values

    return fitness

def combined_rate(generation, structures, objectives, params):
    """
    Computes the overall mutation rate array by combining:
      - Oscillation factor (scalar)
      - Exponential decay factor (scalar)
      - A per-structure fitness factor

    The final rate is:  (oscillation * decay) * fitness

    Parameters
    ----------
    self : object
        Must contain whatever attributes the sub-functions need:
            - self.period, self.amplitude       (for oscillation_factor)
            - self.decay_rate                  (for decay_factor)
            - self.weights, self.temperature    (for fitness_factor)
            etc.
    generation : int
        Current generation index.
    objectives : np.ndarray
        2D array of shape (N, K). One row per structure, one column per objective.

    Returns
    -------
    np.ndarray
        A 1D array of length N giving the final mutation-rate multiplier
        for each structure.
    """
    
    period = params['period']
    decay_rate = params['decay_rate']
    temperature = params['temperature']

    osc = oscillation_factor(generation, period=period)
    dec = decay_factor(generation, decay_rate=decay_rate)
    fit = fitness_factor(objectives=objectives, temperature=temperature)

    combined_scalar = osc * dec  # scalar
    final_rate = combined_scalar * fit  # shape (N,)
    
    final_rate = (final_rate * params['initial_mutation_rate']).astype(np.int32)
    final_rate[final_rate<params['min_mutation_rate']] = params['min_mutation_rate']

    return final_rate

def has_converged(series, N, tolerance):
    """
    Checks if a time series has converged based on the last N values' standard deviation.

    Parameters
    ----------
    series : list or np.ndarray
        The time series data.
    N : int
        Number of last values to check.
    tolerance : float
        The threshold for standard deviation below which we consider convergence.

    Returns
    -------
    bool
        True if converged, False otherwise.
    """
    if len(series) < N:
        return False
    last_values = np.array(series[-N:])
    return np.std(last_values) <= tolerance

def plot_mutation_rate_evolution(
    num_generations: int,
    num_structures: int,
    mutation_rate_params: dict
) -> None:
    """
    Simulates and plots how the final mutation rates evolve over multiple
    generations, based on the provided mutation rate parameters and
    random example objectives.

    Parameters
    ----------
    num_generations : int
        The total number of generations to simulate.
    num_structures : int
        The number of structures to include in each generation.
    mutation_rate_params : dict
        A dictionary containing parameters relevant for computing the final
        mutation rate. Expected keys include:
            - "period" : int
                The period used in the oscillation factor.
            - "decay_rate" : float
                The decay constant for reducing the mutation rate over time.
            - "temperature" : float
                A scaling factor used in the fitness function.
            - "min_mutation_rate" : float
                The lower bound (hard minimum) for the mutation rate.
            - "initial_mutation_rate" : float
                A reference or initial mutation rate (not strictly required
                for the calculation, but useful for initialization if needed).

    Returns
    -------
    None
        This function does not return a value; it simply displays a
        matplotlib plot of the average mutation rate as a function
        of generation.

    Notes
    -----
    - The objectives used here are artificially generated (random values)
      to demonstrate how the mutation rate may evolve. In a real
      implementation, these objectives would be derived from your
      actual physics model or optimization routine.
    - The function assumes the existence of 'combined_rate', 'oscillation_factor',
      'decay_factor', and 'fitness_factor' helper functions, which must be
      defined or imported in the same environment. Make sure you have
      those dependencies satisfied before calling this function.
    """
    import numpy as np
    import matplotlib.pyplot as plt
    import os

    # -------------------------------------------------
    # Main logic of the plotting function
    # -------------------------------------------------
    
    # Pre-allocate arrays to store average, minimum, and maximum rates per generation
    avg_rates = np.zeros(num_generations)
    min_rates = np.zeros(num_generations)
    max_rates = np.zeros(num_generations)

    # Lists to accumulate individual rates for scatter plot
    scatter_gen = []
    scatter_rates = []

    for gen in range(num_generations):
        # Generate dummy 'structures'
        structures = np.arange(num_structures).reshape(-1, 1)

        # Generate random objectives; assume 2 objectives per structure
        objectives = np.random.uniform(low=0.0, high=1.0, size=(num_structures, 2))

        # Compute the final mutation rates using the external combined_rate function
        final_rates = combined_rate(
            generation=gen,
            structures=structures,
            objectives=objectives,
            params=mutation_rate_params
        )

        # Store the average, min, and max of the final rates
        avg_rates[gen] = np.mean(final_rates)
        min_rates[gen] = np.min(final_rates)
        max_rates[gen] = np.max(final_rates)

        # Accumulate individual data for the scatter plot
        scatter_gen.extend([gen] * len(final_rates))
        scatter_rates.extend(final_rates)

    # Calculate the lower and upper error margins for error bars
    lower_errors = avg_rates - min_rates
    upper_errors = max_rates - avg_rates
    yerr = [lower_errors, upper_errors]

    # Create the plot
    plt.figure()
    # Plot the average mutation rate with error bars showing min/max deviation
    plt.errorbar(range(num_generations), avg_rates, yerr=yerr, marker='o',
                 capsize=5, label="Average Mutation Rate")
    # Add a scatter plot for the individual mutation rate data points
    plt.scatter(scatter_gen, scatter_rates, alpha=0.5, color='blue',
                marker='x', label="Individual Mutation Rates")
    plt.xlabel("Generation")
    plt.ylabel("Mutation Rate")
    plt.title("Evolution of Mutation Rate Over Generations")
    plt.grid(True)

    output_dir = '.'
    plot_filename = f"mutation_rate_evolution_estimation.png"
    full_path = os.path.join(output_dir, plot_filename)
    plt.savefig(full_path, dpi=300)
    print(f"Saved plot '{plot_filename}' to: {full_path}")
    plt.close()
