"""Tests for lesson 7 exercises."""

import pytest

from lesson_7.nested_brackets import solution as nested_brackets_solution


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
