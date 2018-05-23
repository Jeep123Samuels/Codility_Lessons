"""Main script for count_divisions.py"""

# Write a function:
#
# def solution(A, B, K)
#
# that, given three integers A, B and K,
# returns the number of integers within the range [A..B] that are divisible by K, i.e.:
#
# { i : A <= i <= B, i mod K = 0 }
#
# For example, for A = 6, B = 11 and K = 2, your function should return 3,
# because there are three numbers divisible by 2 within the range [6..11],
# namely 6, 8 and 10.
#
# Assume that:
#
# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A <= B.
# Complexity:
#
# expected worst-case time complexity is O(1);
# expected worst-case space complexity is O(1).


def solution(A, B, K):
    """Returns the number of integers between range A and B."""
    return (B - (A - (A % K))) // K if A % K else (B - A) // K + 1


if __name__ == "__main__":
    test_array = [0]*100000
    count = -10
    for i in range(0, 100000):
        test_array[i] = count
        count += 1
