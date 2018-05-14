"""Tests for lesson Two."""

import pytest

from lesson_3.frog_jumps import solution as frog_jumps_solution


@pytest.mark.parametrize('init_x,stop_y,jump_len,expected_results', (
    (0, 5, 3, None),
    (8, 0, 3, None),
    (8, 5, 0, None),
    (8, 5, 3, None),
    (5, 13, 5, 2),
    (7, 21, 7, 2),
    (7, 22, 7, 3),
))
def test_array_rotation(init_x, stop_y, jump_len, expected_results):
    """Should rotate arrays as expected."""
    assert frog_jumps_solution(init_x, stop_y, jump_len) == expected_results
