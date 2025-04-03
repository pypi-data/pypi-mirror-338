"""Decorators for conditional execution based on probability distributions."""

import functools
from .distributions import (
    uniform_distribution,
    weighted_distribution,
    normal_distribution,
    exponential_distribution,
    bernoulli_distribution,
    custom_distribution,
)
from .utils import validate_parameters

DISTRIBUTIONS = {
    "uniform": uniform_distribution,
    "weighted": weighted_distribution,
    "normal": normal_distribution,
    "exponential": exponential_distribution,
    "bernoulli": bernoulli_distribution,
    "custom": custom_distribution,
}


def maybe(distribution="uniform", **params):
    """
    Decorator that decides whether to execute the decorated function
    based on a specified probability distribution.

    Parameters:
        distribution (str): The type of distribution to use.
        **params: Parameters specific to the chosen distribution.

    Returns:
        callable: The wrapped function that may or may not execute
        based on the specified distribution.
    """
    if distribution not in DISTRIBUTIONS:
        raise ValueError(f"Unsupported distribution: {distribution}")

    validate_parameters(distribution, params)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            dist_func = DISTRIBUTIONS[distribution]
            execute = dist_func(**params)
            if execute:
                return func(*args, **kwargs)
            else:
                print(f"{func.__name__} did not execute.")
                return None

        return wrapper

    return decorator
