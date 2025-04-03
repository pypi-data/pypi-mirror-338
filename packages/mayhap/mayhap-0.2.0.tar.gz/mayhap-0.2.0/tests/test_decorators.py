"""Tests for the maybe decorator with verbose control."""

from unittest.mock import patch
from io import StringIO
from mayhap.decorators import maybe


# ----------- Uniform Distribution -----------


@patch("mayhap.decorators.uniform_distribution", return_value=True)
def test_maybe_uniform_executes(mock_dist):
    @maybe(distribution="uniform", probability=0.5)
    def test_func():
        return "Executed"

    result = test_func()
    assert result == "Executed"


@patch("mayhap.decorators.uniform_distribution", return_value=False)
@patch("sys.stdout", new_callable=StringIO)
def test_maybe_uniform_skipped_with_verbose_true(mock_stdout, mock_dist):
    @maybe(distribution="uniform", probability=0.5, verbose=True)
    def test_func():
        return "Executed"

    result = test_func()
    assert result is None
    output = mock_stdout.getvalue()
    assert "test_func did not execute." in output


@patch("mayhap.decorators.uniform_distribution", return_value=False)
@patch("sys.stdout", new_callable=StringIO)
def test_maybe_uniform_skipped_with_verbose_false(mock_stdout, mock_dist):
    @maybe(distribution="uniform", probability=0.5, verbose=False)
    def test_func():
        return "Executed"

    result = test_func()
    assert result is None
    output = mock_stdout.getvalue()
    assert "did not execute" not in output


# ----------- Custom Distribution -----------


def test_maybe_custom_executes():
    @maybe(distribution="custom", custom_func=lambda: True)
    def test_func():
        return "Ran"

    assert test_func() == "Ran"


@patch("sys.stdout", new_callable=StringIO)
def test_maybe_custom_skipped_with_verbose_true(mock_stdout):
    @maybe(distribution="custom", custom_func=lambda: False, verbose=True)
    def test_func():
        return "Ran"

    result = test_func()
    assert result is None
    assert "test_func did not execute." in mock_stdout.getvalue()


@patch("sys.stdout", new_callable=StringIO)
def test_maybe_custom_skipped_with_verbose_false(mock_stdout):
    @maybe(distribution="custom", custom_func=lambda: False, verbose=False)
    def test_func():
        return "Ran"

    result = test_func()
    assert result is None
    assert "did not execute" not in mock_stdout.getvalue()
