"""Tests for lesson Two."""

import pytest

from lesson_2.array_rotation import solution as array_rotation_solution


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
