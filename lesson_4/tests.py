"""Tests for lesson 4 exercises."""

import pytest

from lesson_4.frog_river_one import solution as frog_river_one_solution
from lesson_4.missing_integer import solution as missing_integer_solution


@pytest.mark.parametrize('array_test,X,expected_earliest_time', (
    ([1, 2], 3, -1),
    ([2, 2, 2, 2, 2], 2, -1),
    ([-2, 5, 10], 11, -1),
    ([2, 5, 10], 5, -1),
    ([1, 3, 1, 6, 2, 3, 5, 4], 3, -1),
    ([1, 3, 1, 6, 2, 3, 5], 6, -1),
    ([1, 3, 1, 6, 2, 3, 5, 4], 6, 7),
    ([1, 4, 1, 2, 3, 5, 4], 5, 5),
    ([1, 4, 1, 2, 3, 2, 5, 4], 5, 6),
))
def test_solution_for_calculating_earliest_time(array_test, X, expected_earliest_time):
    """Should return the earliest time 1+2+3+...(a+1)...+X is completed."""
    # when ... solution function called
    # then ... returned earliest time is as expected.
    assert frog_river_one_solution(X, array_test) == expected_earliest_time


@pytest.mark.parametrize('array_test,expected_smallest_integer', (
    ([], 1),
    ([0], 1),
    ([10], 1),
    ([-1, -3], 1),
    ([0, 2, 5], 1),
    ([-2, -2, -2, -2, -2], 1),
    ([1, 1, 3, 5, 4, -1, -13], 2),
    ([1, 4, 1, 2, 3, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 20], 13),
))
def test_solution_for_getting_smallest_missing_integer(array_test, expected_smallest_integer):
    """Should return the smallest missing positive integer in the given array."""
    # when ... solution function called
    # then ... returned smallest positive integer is as expected.
    assert missing_integer_solution(array_test) == expected_smallest_integer
