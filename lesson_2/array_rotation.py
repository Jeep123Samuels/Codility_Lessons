"""Main script for array_rotation.py"""

# An array A consisting of N integers is given.
# Rotation of the array means that each element
# is shifted right by one index, and the last element
# of the array is moved to the first place.
# For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7]
# (elements are shifted right by one index and 6 is moved to the first place).
#
# The goal is to rotate array A K times;
# that is, each element of A will be shifted to the right K times.
#
# Write a function:
#
# def solution(A, K)
#
# that, given an array A consisting of N integers and an integer K,
# returns the array A rotated K times.


def solution(N, K):
    """Returns rotated array where N is array and K number of rotations."""
    if not N:
        return []
    a = K % len(N)
    return N[-a:] + N[:-a]


if __name__ == "__main__":
    array_test = ['1', 'a', '23', 'sada', 'sad']
    K = 2
    print(solution(array_test, K))
