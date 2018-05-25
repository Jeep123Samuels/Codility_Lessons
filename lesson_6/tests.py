"""Tests for lesson 5 exercises."""

import pytest

from lesson_6.max_product_of_three import solution as max_product_of_three_solution


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
