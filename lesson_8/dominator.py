"""Main script for dominator.py"""

# An array A consisting of N integers is given.
# The dominator of array A is the value that occurs in more than half of the elements of A.
#
# For example, consider array A such that
#
#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# The dominator of A is 3 because it occurs in 5 out of 8 elements of A
# (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.
#
# Write a function
#
# def solution(A)
#
# that, given an array A consisting of N integers,
# returns index of any element of array A in which
# the dominator of A occurs.
# The function should return −1 if array A does not have a dominator.
#
# Assume that:
#
# N is an integer within the range [0..100,000];
# each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
# For example, given array A such that
#
#  A[0] = 3    A[1] = 4    A[2] =  3
#  A[3] = 2    A[4] = 3    A[5] = -1
#  A[6] = 3    A[7] = 3
# the function may return 0, 2, 4, 6 or 7, as explained above.
#
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(1) (not counting the storage required for input arguments).


def solution(S):
    """Returns last index of the dominator or -1 if non exist."""
    from collections import defaultdict

    def init_to_zero():
        return 0

    N = len(S)
    if N < 1:
        return -1
    # create a queue with the first value in array.
    queue_ = [S[0]]
    last_index = 0

    # Remember the count using pigeon hole with defaultdict.
    counting = defaultdict(init_to_zero)
    counting[S[0]] = 1
    # Iterate through given array.
    # If current value in array not equal to the last added value, pop,
    # else we add the value to the tail of the queue.
    for i in range(1, N):
        counting[S[i]] += 1
        if queue_ and S[i] != queue_[-1]:
            queue_.pop()
        else:
            queue_.append(S[i])
            last_index = i
    if queue_ and counting[S[last_index]] > N//2:
        return last_index
    return -1

if __name__ == "__main__":
    # solution()
    a = list()
    a.append('a')
    print(a)
    a.append('b')
    print(a)
    a.append('c')
    print(a)
