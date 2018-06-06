"""Tests for lesson 6 exercises."""

import pytest

from lesson_6.max_product_of_three import solution as max_product_of_three_solution
from lesson_6.merge_sort_algorithm import halve_sort, merge
from lesson_6.triangle import solution as triangle_solution


@pytest.mark.parametrize('test_array,expected_product', (
    ([-3, -1, -2, 5, 6], 36),
    ([-3, 0, 0, 5, 6], 0),
    ([-3, 1, 2, -2, 5, 6], 60),
    ([-3, 1, 2, -2, 5, 6], 60),
    ([-3, 1, 2, 5, 6], 60),
    ([6, 1, 2, 5], 60),
    ([6, 1, 1, 5], 30),
    ([6, 0, 0, 5], 0),
))
def test_max_product_of_three_returns_maximum_combo_of_products(
    test_array,
    expected_product,
):
    """Should return the maximum product in the array of any combination."""
    # when ... solution function called
    # then ... returned the max product
    assert max_product_of_three_solution(test_array) == expected_product


@pytest.mark.parametrize('left_array,right_array,expected_array', (
    ([20], [10], [10, 20]),
    ([1, 2], [3, 4], [1, 2, 3, 4]),
    ([1, 4], [2, 3], [1, 2, 3, 4]),
    ([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6]),
    ([1, 3, 4], [2, 5], [1, 2, 3, 4, 5]),
))
def test_merge_function_returns_ordered_array_if_given_two_ordered_lists(
    left_array,
    right_array,
    expected_array,
):
    """Should return ordered list if given two ordered lists."""
    # when ... solution function called
    # then ... returned a ordered list
    assert merge(left_array, right_array) == expected_array


@pytest.mark.parametrize('given_array,expected_sorted_array', (
    ([4, 1, 2, 3], [1, 2, 3, 4]),
    ([3, 1, 2, 4], [1, 2, 3, 4]),
    ([6, 2, 3, 4, 5, 1], [1, 2, 3, 4, 5, 6]),
    ([1, 4, 5, 2, 3, 6], [1, 2, 3, 4, 5, 6]),
    ([1, 3, 4, 2, 5], [1, 2, 3, 4, 5]),
))
def test_halve_sort_returns_two_ordered_lists(
    given_array,
    expected_sorted_array,
):
    """Should return two ordered lists."""
    # when ... solution function called
    # then ... returned two ordered lists
    assert halve_sort(given_array) == expected_sorted_array


@pytest.mark.parametrize('given_array,expected_sorted_array', (
    ([4, 1, 2, 3], [1, 2, 3, 4]),
    ([3, 1, 2, 4], [1, 2, 3, 4]),
    ([6, 2, 3, 4, 5, 1], [1, 2, 3, 4, 5, 6]),
    ([1, 4, 5, 2, 3, 6], [1, 2, 3, 4, 5, 6]),
    ([1, 3, 4, 2, 5], [1, 2, 3, 4, 5]),
))
def test_halve_sort_returns_two_ordered_lists(
    given_array,
    expected_sorted_array,
):
    """Should return two ordered lists."""
    # when ... solution function called
    # then ... returned two ordered lists
    assert halve_sort(given_array) == expected_sorted_array


@pytest.mark.parametrize('given_array,expected_return', (
    ([4, 1, 2, 3], 1),
    ([3, 1, 2, 4], 1),
    ([-6, 2, 3, -24, 5, 1], 0),
))
def test_triangle_is_detected_in_set_of_integers(
    given_array,
    expected_return,
):
    """Should return True if triangle in set of points."""
    # when ... solution function called
    # then ... returns if triangle possible
    assert triangle_solution(given_array) == expected_return
