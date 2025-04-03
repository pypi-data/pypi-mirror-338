"""Distributions module for generating random numbers based on various distributions."""

import random


def uniform_distribution(probability=0.5):
    """
    Generates a random number and compares it to a given probability.
    If the random number is less than the probability, returns True,
    otherwise returns False.
    """
    return random.random() < probability


def weighted_distribution(weights=[1, 1]):
    """
    Generates a random choice based on given weights.
    If the random choice is based on the first weight, returns True,
    otherwise returns False.
    """
    return random.choices([True, False], weights=weights)[0]


def normal_distribution(mean=0.5, stddev=0.1):
    """
    Generates a random number from a normal distribution with the given
    mean and standard deviation. If the random number is less than
    the mean, returns True, otherwise returns False.
    """
    probability = random.gauss(mean, stddev)
    return random.random() < probability


def exponential_distribution(lambd=1.0):
    """
    Generates a random number from an exponential distribution with the
    given lambda. If the random number is less than the lambda,
    returns True, otherwise returns False.
    """
    probability = random.expovariate(lambd)
    return random.random() < probability


def bernoulli_distribution(p=0.5):
    """
    Generates a random number from a Bernoulli distribution with the
    given probability p. If the random number is less than p,
    returns True, otherwise returns False.
    """
    return random.random() < p


def custom_distribution(custom_func):
    """
    Executes a custom function to determine whether to execute the
    decorated function. The custom function should return True or
    False.
    """
    if callable(custom_func):
        return custom_func()
    else:
        raise ValueError("Custom function must be callable.")
