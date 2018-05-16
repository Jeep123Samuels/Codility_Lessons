"""Tests for lesson Two."""

import pytest

from lesson_3.frog_jumps import solution as frog_jumps_solution
from lesson_3.permutation_missing import solution as permutation_missing_solution
from lesson_3.tape_equilibrium import solution as tape_equilibrium_solution


@pytest.mark.parametrize('init_x,stop_y,jump_len,expected_results', (
    (0, 5, 3, None),
    (8, 0, 3, None),
    (8, 5, 0, None),
    (8, 5, 3, None),
    (5, 13, 5, 2),
    (7, 21, 7, 2),
    (7, 22, 7, 3),
))
def test_frog_jumps_returns_minimum_required_jumps(init_x, stop_y, jump_len, expected_results):
    """Should return the minimum required jumps to reach endpoint."""
    assert frog_jumps_solution(init_x, stop_y, jump_len) == expected_results


@pytest.mark.parametrize('array_test,expected_results', (
    ([], 1),
    ([1], 2),
    ([2], 1),
    ([2, 1], 3),
    ([2, 3], 1),
    ([1, 2, 1], 0),
    ([1, 2, 3, 4, 6], 5),
    ([1, 3, 4, 5, 6], 2),
    ([2, 3, 4, 5, 6], 1),
    ([1, 2, 3, 4, 5], 6),
))
def test_permutation_missing_value(array_test, expected_results):
    """Should return the missing value in 1..N+1 sequence."""
    assert permutation_missing_solution(array_test) == expected_results


@pytest.mark.parametrize('array_test,expected_results', (
    ([], 0),
    ([1], 1),
    ([2], 2),
    ([2, 8], 6),
    ([2, 100000], 0),
    ([2, -300000], 0),
    ([3, 1, 2, 4, 3], 1),
))
def test_tape_equilibrium_solution_getting_smallest_difference(array_test, expected_results):
    """Should return the smallest difference between each half of array."""
    assert tape_equilibrium_solution(array_test) == expected_results
