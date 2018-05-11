"""Tests for binary gap calculation."""

import pytest

from lesson_1.binary_gaps import solution


@pytest.mark.parametrize('binary_strings,expected_gap', (
    ('10001', 3),
    ('1010101', 1),
    ('1001111', 2),
    ('100000001', 7),
    ('1100110011', 2),
    ('11111', 0),
))
def test_solution_for_calculating_binary_gaps(binary_strings, expected_gap):
    """Should on calling solution calculate the expected binary gap."""
    # when ... solution function called
    # then ... returned binary gap is as expected.
    assert solution(binary_strings) == expected_gap
