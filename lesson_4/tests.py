"""Tests for lesson 4 exercises."""

import pytest

from lesson_4.frog_river_one import solution as frog_river_one_solution
from lesson_4.max_counters import solution as max_counters_solution
from lesson_4.missing_integer import solution as missing_integer_solution
from lesson_4.permutation_check import solution as permutation_check_solution


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


@pytest.mark.parametrize('array_test,expected_result', (
    # Given
    # ... arrays that are not permutation
    ([1, 3, 4], 0),
    ([1, 4, 2, 3, 7, 9, 6], 0),
    ([100000], 0),
    # ... and those arrays that are.
    ([1], 1),
    ([1, 2, 3, 4], 1),
    ([1, 4, 2, 3], 1),
    ([8, 1, 4, 2, 3, 7, 9, 6, 5], 1),
))
def test_solution_determines_an_array_as_permutation(array_test, expected_result):
    """Should return whether array is a permutation or not."""
    # when ... solution function called
    # then ... returned smallest positive integer is as expected.
    assert permutation_check_solution(array_test) == expected_result


@pytest.mark.parametrize('array_test,n_counter,expected_result', (
    # Given
    # ... arrays that are in [1+...+N+1] range.
    ([1], 3, [1, 0, 0]),
    ([4], 3, [0, 0, 0]),
    ([1, 2, 4, 2], 3, [1, 2, 1]),
    ([1, 2, 2, 4], 3, [2, 2, 2]),
    ([3, 4, 4, 6, 1, 4, 4], 5, [3, 2, 2, 4, 2]),
))
def test_solution_max_counters_solution(array_test, n_counter, expected_result):
    """Should return max_counters according to the described algorithm.

    Given an array (counter) [0]*n_counter:
    if 1 <= array_test[n_counter] <= n_counter:
        then counter[array_test[n_counter]-1] += 1
    if array_test[n_counter] == n_counter + 1:
        then counter[ALL] == max(counter[])
    """
    # when ... solution function called
    # then ... returned counter matrix for algorithm.
    assert max_counters_solution(n_counter, array_test) == expected_result
