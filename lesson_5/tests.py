"""Tests for lesson 4 exercises."""

import pytest

from lesson_5.count_divisions import solution as count_divisions_solution


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
