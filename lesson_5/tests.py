"""Tests for lesson 4 exercises."""

import pytest

from lesson_5.count_divisions import solution as count_divisions_solution
from lesson_5.passing_cars import solution as passing_cars_solution
from lesson_5.genomic_range_query import solution as genomic_range_query_solution


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


@pytest.mark.parametrize('binary_array,expected_passes', (
    ([0, 0, 0], 0),
    ([0, 1, 0, 1, 1], 5),
    ([0, 1, 1, 1, 1], 4),
    ([0, 1, 0, 0, 1], 4),
    ([0, 1, 0, 0, 0], 1),
    ([0, 1, 1, 0, 0, 0], 2),
))
def test_solution_returns_the_number_of_passing_cars(binary_array, expected_passes):
    """Should return the number of passing cars."""
    # when ... passing_cars_solution function called
    # then ... returned the number of integers divisible the
    assert passing_cars_solution(binary_array) == expected_passes

#     P[0] = 2    Q[0] = 4
#     P[1] = 5    Q[1] = 5
#     P[2] = 0    Q[2] = 6
@pytest.mark.parametrize('gene_array,P,Q,expected_passes', (
    ('AAAAA', [0, 2, 4], [4, 4, 4], [1, 1, 1]),
    ('GGTGAG', [0, 2, 2], [3, 5, 2], [3, 1, 4]),
    ('CAGCCTA', [2, 5, 0], [4, 5, 6], [2, 4, 1]),
    ('AAAAAAAAAAGAAAAATAAAAA', [0, 2, 15, 13], [21, 4, 15, 21], [1, 1, 1, 1]),
))
def test_solution_returns_factor_number_for_genomic_range_query(
    gene_array,
    P,
    Q,
    expected_passes
):
    """Should return the factor number for genomic range query."""
    # when ... solution function called
    # then ... returned the number of integers divisible the
    assert genomic_range_query_solution(gene_array, P, Q) == expected_passes
