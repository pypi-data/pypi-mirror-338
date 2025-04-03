"""Tests for the utils module."""

import pytest
from mayhap.utils import validate_parameters


def test_validate_parameters():
    # Valid parameters
    validate_parameters("uniform", {"probability": 0.5})
    validate_parameters("weighted", {"weights": [1, 2]})
    validate_parameters("normal", {"mean": 0.5, "stddev": 0.1})
    validate_parameters("exponential", {"lambd": 1.0})
    validate_parameters("bernoulli", {"p": 0.5})
    validate_parameters("custom", {"custom_func": lambda: True})

    # Invalid parameters
    with pytest.raises(ValueError):
        validate_parameters("uniform", {"probability": 1.5})
    with pytest.raises(ValueError):
        validate_parameters("weighted", {"weights": [-1, 2]})
    with pytest.raises(ValueError):
        validate_parameters("normal", {"mean": 0.5, "stddev": -0.1})
    with pytest.raises(ValueError):
        validate_parameters("exponential", {"lambd": -1.0})
    with pytest.raises(ValueError):
        validate_parameters("bernoulli", {"p": 1.5})
    with pytest.raises(ValueError):
        validate_parameters("custom", {"custom_func": None})
