"""Tests for lesson Two."""

import pytest

from lesson_2.array_rotation import solution as array_rotation_solution
from lesson_2.odd_occurrence import solution as odd_occurrence_solution


@pytest.mark.parametrize('array_test,rotations,expected_results', (
    ([], 3, []),
    (['1', '2', '3', '4', '5', '6'], 1, ['6', '1', '2', '3', '4', '5']),
    (['1', '2', '3', '4', '5', '6'], 3, ['4', '5', '6', '1', '2', '3']),
    (['1', '2', '3', '4', '5', '6'], 6, ['1', '2', '3', '4', '5', '6']),
    (['1', '2', '3', '4', '5', '6'], 10, ['3', '4', '5', '6', '1', '2']),
    (['1', '2', '3', '4', '5', '6'], 12, ['1', '2', '3', '4', '5', '6']),
))
def test_array_rotation(array_test, rotations, expected_results):
    """Should rotate arrays as expected."""
    assert array_rotation_solution(array_test, rotations) == expected_results


@pytest.mark.parametrize('array_test,expected_results', (
    ([], 0),
    ([1, 2, 1], 2),
    ([1, 2, 3, 2, 1], 3),
    ([5, 1, 3, 1, 2, 2, 3], 5),
    ([1, 7, 1, 1, 1], 7),
    ([1, 1, 2, 10, 8, 2, 8], 10),
    ([1, 1, 2, 8, 2, 8], 0),
    ([9, 3, 9, 3, 9, 7, 9], 7),
))
def test_odd_occurrence_in_array(array_test, expected_results):
    """Should return the value odd occurring in an array."""
    assert odd_occurrence_solution(array_test) == expected_results
