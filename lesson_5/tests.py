"""Tests for lesson 4 exercises."""

import pytest

from lesson_5.count_divisions import solution as count_divisions_solution
from lesson_5.passing_cars import solution as passing_cars_solution


@pytest.mark.parametrize('start_integer,end_integer,K,expected_integers', (
    (0, 0, 2, 0),
    (4, 4, 2, 1),
    (4, 5, 3, 0),
    (6, 11, 2, 3),
    (10, 10, 5, 1),
    (22, 22, 11, 1),
))
def test_solution_for_number_of_integers_divisible_by_given_integer(
    start_integer,
    end_integer,
    K,
    expected_integers
):
    """Should return the number of integers divisible by K."""
    # when ... solution function called
    # then ... returned the number of integers divisible the
    assert count_divisions_solution(start_integer, end_integer, K) == expected_integers


@pytest.mark.parametrize('binary_array,expected_passes', (
    ([0, 0, 0], 0),
    ([0, 1, 0, 1, 1], 5),
    ([0, 1, 1, 1, 1], 4),
    ([0, 1, 0, 0, 1], 4),
    ([0, 1, 0, 0, 0], 1),
    ([0, 1, 1, 0, 0, 0], 2),
))
def test_solution_returns_the_number_of_passing_cars(binary_array, expected_passes):
    """Should return the number of passing cars."""
    # when ... solution function called
    # then ... returned the number of integers divisible the
    assert passing_cars_solution(binary_array) == expected_passes
