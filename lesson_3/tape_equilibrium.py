"""Main script for tape_equilibrium.py"""


# A non-empty array A consisting of N integers is given. Array A represents numbers on a tape.
#
# Any integer P, such that 0 < P < N,
# splits this tape into two non-empty parts: A[0], A[1], ..., A[P - 1] and A[P], A[P + 1], ..., A[N - 1].
#
# The difference between the two parts is the value of:
# |(A[0] + A[1] + ... + A[P - 1]) - (A[P] + A[P + 1] + ... + A[N - 1])|
#
# In other words, it is the absolute difference between the sum of the first part and the sum of the second part.
#
# For example, consider array A such that:
#
#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# We can split this tape in four places:
#
# P = 1, difference = |3 - 10| = 7
# P = 2, difference = |4 - 9| = 5
# P = 3, difference = |6 - 7| = 1
# P = 4, difference = |10 - 3| = 7
# Write a function:
#
# def solution(A)
#
# that, given a non-empty array A of N integers, returns the minimal difference that can be achieved.
#
# For example, given:
#
#   A[0] = 3
#   A[1] = 1
#   A[2] = 2
#   A[3] = 4
#   A[4] = 3
# the function should return 1, as explained above.
#
# Assume that:
#
# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [-1,000..1,000].
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N) (not counting the storage required for input arguments).


def solution(A):
    """Returns smallest absolute difference for each array splice."""
    N = len(A)
    if N == 0 or N > 100000 or max(A) > 1000 or min(A) < -1000:
        return 0
    if N == 1:
        return A[0]

    current_diff = 1000000
    sum_to_left = A[0]
    A = A[1:]
    sum_to_right = sum(A)
    for i in range(0, len(A)):
        hold = abs(sum_to_left - sum_to_right)
        if hold < current_diff:
            current_diff = hold
        sum_to_right -= A[i]
        sum_to_left += A[i]
    return current_diff

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    print(sum(a[1:]))
    print(sum(a[:1]))
    print(abs(2-4))
