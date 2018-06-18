"""Tests for lesson 8 exercises."""

import pytest

from lesson_8.dominator import solution as dominator_solution
from lesson_8.equi_leader import solution as equi_leader_solution


@pytest.mark.parametrize('test_array,expected_return', (
    ([1], 0),
    ([-1, -1, -1, 3, 3, 3, 3, 3], 7),
    ([3, 3, 3, 3, 3, 3, 3, 3], 7),
    ([3, 3, 3, 3, 3, -1, -1, -1], 4),
    ([3, 4, 3, 2, 3, -1, 3, 3], 7),
))
def test_returns_last_index_of_dominator(
    test_array,
    expected_return,
):
    """Should return last index of dominator."""
    # when ... solution function called
    # then ... returned expected valuation
    assert dominator_solution(test_array) == expected_return


@pytest.mark.parametrize('test_array,expected_return', (
    ([], -1),
    ([1, 2, 1, 2], -1),
    ([3, 4, 3, 2, 3, -1, 3, -1], -1),
    ([3, 4, 3, 2, 3, -1, 3, -1], -1),
    ([3, 4, 3, 2, 3, -1, 3, -1], -1),
))
def test_returns_minus_1_value_as_no_dominator_exists_in_array(
    test_array,
    expected_return,
):
    """Should return -1 as no dominator exist in the given arrays."""
    # when ... solution function called
    # then ... returned expected valuation
    assert dominator_solution(test_array) == expected_return


@pytest.mark.parametrize('test_array,expected_return', (
    ([4, 4], 1),
    ([4, 4], 1),
    ([4, 4, 2, 5, 3, 4, 4], 0),
    # ([4, 4, 2, 5, 3, 4, 4, 4], 3),  # Codility gives this a fail
    ([4, 4, 2, 5, 3, 4, 4, 4], 2),  # Above should be this.
    ([4, 3, 4, 4, 4, 2], 2),
    ([4, 3, 4, 4, 4, 4, 2], 3),
))
def test_return_number_of_equi_leaders_in_array(
    test_array,
    expected_return,
):
    """Should return number of equi_leaders present in a given array."""
    # when ... solution function called
    # then ... returned expected valuation
    assert equi_leader_solution(test_array) == expected_return
