"""Main script for permutation_missing.py"""


# An array A consisting of N different integers is given.
# The array contains integers in the range [1..(N + 1)],
# which means that exactly one element is missing.
#
# Your goal is to find that missing element.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A, returns the value of the missing element.
#
# For example, given array A such that:
#
#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.
#
# Assume that:
# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(1) (not counting the storage required for input arguments).


def solution(A):
    """Returns missing permutation number from array."""
    if not A:
        return 1
    A.sort()
    if A[0] != 1:
        return 1
    if len(A) == 1 and A[0] == 1:
        return 2
    if len(A) == A[-1]:
        return A[-1] + 1

    for i in range(1, len(A)):
        hold = A[i] - A[i-1]
        if hold != 1:
            return A[i] - 1

if __name__ == "__main__":
    print(solution([1, 3, 5, 7, 11, 13]))
