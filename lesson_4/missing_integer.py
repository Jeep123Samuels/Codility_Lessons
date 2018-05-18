"""Main script for missing_integer.py"""

# Write a function:
#
# def solution(A)
#
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
#
# Given A = [1, 2, 3], the function should return 4.
#
# Given A = [−1, −3], the function should return 1.
#
# Assume that:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N) (not counting the storage required for input arguments).


def solution(A):
    """Returns the smallest missing integer in the given sequence/array."""
    if not A:
        return 1
    N = len(A)
    max_N = max(A)
    if max_N < 0:
        return 1
    if N < 0 or N > 100000:
        return -1
    count_array = [0] * (max_N+1)
    for value in A:
        value -= 1
        if value > -1 and not count_array[value]:
            count_array[value] = 1
    return count_array.index(0) + 1


if __name__ == "__main__":
    test_array = [0]*100000
    count = -10
    for i in range(0, 100000):
        test_array[i] = count
        count += 1
