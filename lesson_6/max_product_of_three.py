"""Main script for max_product_of_three.py"""

# A non-empty array A consisting of N integers is given.
# The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 <= P < Q < R < N).
#
# For example, array A such that:
#
#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# contains the following example triplets:
#
# (0, 1, 2), product is -3 * 1 * 2 = -6
# (1, 2, 4), product is 1 * 2 * 5 = 10
# (2, 4, 5), product is 2 * 5 * 6 = 60
# Your goal is to find the maximal product of any triplet.
#
# Write a function:
#
# def solution(A)
#
# that, given a non-empty array A, returns the value of the maximal product of any triplet.
#
# For example, given array A such that:
#
#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# the function should return 60, as the product of triplet (2, 4, 5) is maximal.
#
# Assume that:
#
# N is an integer within the range [3..100,000];
# each element of array A is an integer within the range [-1,000..1,000].
# Complexity:
#
# expected worst-case time complexity is O(N*log(N));
# expected worst-case space complexity is O(1) (not counting the storage required for input arguments).


def solution(A):
    """Returns the maximum product count of three combination in the array."""
    A.sort()
    max_product = A[-3] * A[-2] * A[-1]
    if len(A) == 3:
        return max_product
    if A[1] < 0 and max_product < A[0] * A[1] * A[-1]:
        return A[0] * A[1] * A[-1]
    return max_product


if __name__ == "__main__":
    test_array = [0]*100000
    count = -10
    for i in range(0, 100000):
        test_array[i] = count
        count += 1
