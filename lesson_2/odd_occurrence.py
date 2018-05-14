"""Main script for odd_occurrence.py"""

# A non-empty array A consisting of N integers is given.
# The array contains an odd number of elements,
# and each element of the array can be paired with another
# element that has the same value, except for one element that is left unpaired.
#
# For example, in array A such that:
#
#   A[0] = 9  A[1] = 3  A[2] = 9
#   A[3] = 3  A[4] = 9  A[5] = 7
#   A[6] = 9
# the elements at indexes 0 and 2 have value 9,
# the elements at indexes 1 and 3 have value 3,
# the elements at indexes 4 and 6 have value 9,
# the element at index 5 has value 7 and is unpaired.
# Assume that:
#
# N is an odd integer within the range [1..1,000,000];
# each element of array A is an integer within the range [1..1,000,000,000];
# all but one of the values in A occur an even number of times.


def solution(A):
    """Returns the odd un-pair value in an array."""
    N = len(A)
    if not N or (N % 2) != 1 or N < 1 or N > 1000000:
        return 0
    missing_int = 0
    for x in A:
        if x < 1 or x > 1000000000:
            return 0
        missing_int ^= x
    return missing_int


if __name__ == "__main__":
    a = [1, 2, 3, 2, 1]
    solution(a)
