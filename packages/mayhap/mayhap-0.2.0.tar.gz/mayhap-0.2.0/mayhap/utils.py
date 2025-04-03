"""Utility functions for Mayhap."""


def validate_parameters(distribution, params):
    """
    Validates parameters for the specified distribution.

    Parameters:
        distribution (str): The type of distribution.
        params (dict): Parameters specific to the chosen distribution.

    Raises:
        ValueError: If any parameter is invalid.
    """
    if distribution == "uniform":
        probability = params.get("probability", 0.5)
        if not (0 <= probability <= 1):
            raise ValueError("Probability must be between 0 and 1.")

    elif distribution == "weighted":
        weights = params.get("weights", [1, 1])
        if not all(w >= 0 for w in weights):
            raise ValueError("Weights must be non-negative.")

    elif distribution == "normal":
        stddev = params.get("stddev", 0.1)
        if stddev < 0:
            raise ValueError("Standard deviation must be non-negative.")

    elif distribution == "exponential":
        lambd = params.get("lambd", 1.0)
        if lambd <= 0:
            raise ValueError("Lambda must be positive.")

    elif distribution == "bernoulli":
        p = params.get("p", 0.5)
        if not (0 <= p <= 1):
            raise ValueError("Probability must be between 0 and 1.")

    elif distribution == "custom":
        custom_func = params.get("custom_func")
        if not callable(custom_func):
            raise ValueError("Custom function must be callable.")
