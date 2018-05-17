"""Tests for binary gap calculation."""

import pytest

from lesson_4.frog_river_one import solution as frog_river_one_solution


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
def test_solution_for_calculating_binary_gaps(array_test, X, expected_earliest_time):
    """Should return the earliest time 1+2+3+...(a+1)...+X is completed."""
    # when ... solution function called
    # then ... returned binary gap is as expected.
    assert frog_river_one_solution(X, array_test) == expected_earliest_time
