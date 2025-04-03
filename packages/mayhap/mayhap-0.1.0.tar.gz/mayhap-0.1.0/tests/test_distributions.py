"""Tests for the distributions module."""

import pytest
from unittest.mock import patch
from mayhap.distributions import (
    uniform_distribution,
    weighted_distribution,
    normal_distribution,
    exponential_distribution,
    bernoulli_distribution,
    custom_distribution,
)


def test_uniform_distribution():
    with patch("random.random", return_value=0.3):
        assert uniform_distribution(probability=0.5) is True
    with patch("random.random", return_value=0.6):
        assert uniform_distribution(probability=0.5) is False


def test_weighted_distribution():
    with patch("random.choices", return_value=[True]):
        assert weighted_distribution(weights=[3, 1]) is True
    with patch("random.choices", return_value=[False]):
        assert weighted_distribution(weights=[1, 3]) is False


def test_normal_distribution():
    with (
        patch("random.gauss", return_value=0.4),
        patch("random.random", return_value=0.3),
    ):
        assert normal_distribution(mean=0.5, stddev=0.1) is True
    with (
        patch("random.gauss", return_value=0.6),
        patch("random.random", return_value=0.7),
    ):
        assert normal_distribution(mean=0.5, stddev=0.1) is False


def test_exponential_distribution():
    with (
        patch("random.expovariate", return_value=0.4),
        patch("random.random", return_value=0.3),
    ):
        assert exponential_distribution(lambd=1.0) is True
    with (
        patch("random.expovariate", return_value=0.6),
        patch("random.random", return_value=0.7),
    ):
        assert exponential_distribution(lambd=1.0) is False


def test_bernoulli_distribution():
    with patch("random.random", return_value=0.3):
        assert bernoulli_distribution(p=0.5) is True
    with patch("random.random", return_value=0.6):
        assert bernoulli_distribution(p=0.5) is False


def test_custom_distribution():
    assert custom_distribution(lambda: True) is True
    assert custom_distribution(lambda: False) is False
    with pytest.raises(ValueError):
        custom_distribution(None)
