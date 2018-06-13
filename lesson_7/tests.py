"""Tests for lesson 7 exercises."""

import pytest

from lesson_7.fish_swimming import solution as fish_swimming_solution
from lesson_7.nested_brackets import solution as nested_brackets_solution
from lesson_7.nested_brackets_revisit import solution as nested_brackets_revisit_solution


@pytest.mark.parametrize('test_string,expected_bool', (
    ('', True),
    ('[]{}()', True),
    ('[]{}(', False),
    ('[]{}($', False),
    ('[]a}()', False),
    ('{[()()]}', True),
    ('{[{)()]}', False),
    ('}[{}()]{', False),
    ('{{{{', False),
))
def test_nested_brackets_solution_properly_validates_strings(
    test_string,
    expected_bool,
):
    """Should return True for all nested bracket strings."""
    # when ... solution function called
    # then ... returned expected valuation
    assert nested_brackets_solution(test_string) == expected_bool


@pytest.mark.parametrize('array_A,array_B,expected_array', (
    ([4, 3, 2, 1, 5], [1, 1, 1, 1, 0], [5]),
    ([4, 3, 2, 1, 5], [1, 0, 0, 0, 0], [5]),
    ([4, 3, 2, 1, 5], [0, 1, 1, 1, 0], [4, 5]),
    ([4, 3, 2, 1, 5], [0, 1, 0, 1, 0], [4, 5]),
    ([4, 3, 2, 1, 5], [0, 1, 0, 0, 0], [4, 5]),
    ([4, 3, 2, 1, 5], [0, 0, 1, 0, 0], [4, 3, 5]),
    ([4, 3, 2, 1, 5], [0, 0, 0, 1, 0], [4, 3, 2, 5]),
    ([4, 3, 2, 1, 5], [0, 0, 0, 0, 1], [4, 3, 2, 1, 5]),
    ([4, 3, 2, 1, 5], [1, 1, 1, 1, 1], [4, 3, 2, 1, 5]),
    (
        [4, 3, 2, 1, 5, 7, 9, 15, 6, 8, 20, 11],
        [0, 0, 0, 0, 1, 1, 1,  1, 1, 1,  1,  1],
        [4, 3, 2, 1, 5, 7, 9, 15, 6, 8, 20, 11],
    ),
))
def test_correctly_filters_array_with_remaining_numbers(
    array_A,
    array_B,
    expected_array,
):
    """Should return array of the remaining values in the array."""
    # when ... solution function called
    # then ... returned expected array
    assert fish_swimming_solution(array_A, array_B) == expected_array


@pytest.mark.parametrize('test_string,expected_bool', (
    ('', True),
    ('()', True),
    ('(', False),
    ('($', False),
    ('()a}()', False),
    ('((()()))', True),
    ('((()())', False),
    (')(()())(', False),
    ('((((', False),
    ('(()(())())', True),
))
def test_nested_brackets_revisit_solution_properly_validates_strings(
    test_string,
    expected_bool,
):
    """Should return True for all nested bracket strings."""
    # when ... solution function called
    # then ... returned expected valuation
    assert nested_brackets_revisit_solution(test_string) == expected_bool
