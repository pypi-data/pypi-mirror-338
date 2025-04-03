"""Tests for the decorators module."""

from unittest.mock import patch
from mayhap.decorators import maybe


def test_maybe_uniform():
    @maybe(distribution="uniform", probability=0.5)
    def test_func():
        return "Executed"

    with patch("random.random", return_value=0.3):
        assert test_func() == "Executed"
    with patch("random.random", return_value=0.6):
        assert test_func() is None


def test_maybe_weighted():
    @maybe(distribution="weighted", weights=[3, 1])
    def test_func():
        return "Executed"

    with patch("random.choices", return_value=[True]):
        assert test_func() == "Executed"
    with patch("random.choices", return_value=[False]):
        assert test_func() is None


def test_maybe_custom():
    def always_true():
        return True

    def always_false():
        return False

    @maybe(distribution="custom", custom_func=always_true)
    def test_func_true():
        return "Executed"

    @maybe(distribution="custom", custom_func=always_false)
    def test_func_false():
        return "Executed"

    assert test_func_true() == "Executed"
    assert test_func_false() is None
