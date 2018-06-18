"""Main script for equi_leader.py"""

# A non-empty array A consisting of N integers is given.
#
# The leader of this array is the value that occurs in more than half of the elements of A.
#
# An equi leader is an index S such that 0 ≤ S < N − 1 and
# two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.
#
# For example, given array A such that:
#
#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# we can find two equi leaders:
#
# 0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
# 2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
# The goal is to count the number of equi leaders.
#
# Write a function:
#
# def solution(A)
#
# that, given a non-empty array A consisting of N integers, returns the number of equi leaders.
#
# For example, given:
#
#     A[0] = 4
#     A[1] = 3
#     A[2] = 4
#     A[3] = 4
#     A[4] = 4
#     A[5] = 2
# the function should return 2, as explained above.
#
# Assume that:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N) (not counting the storage required for input arguments).


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
        leader_count = counting[S[last_index]]
    else:
        return 0
    eq_leader_count = 0
    current_leader_count = 0
    for i in range(N-1):
        # if value is the current leader.
        if S[i] == S[last_index]:
            current_leader_count += 1
            if (current_leader_count > (i+1)//2 and
                    (leader_count-current_leader_count) > (N-(i+1))//2):
                eq_leader_count += 1
    return eq_leader_count

if __name__ == "__main__":
    solution([4, 3, 4, 4, 4, 4, 2])
    a = list()
    a.append('a')
    print(a)
    a.append('b')
    print(a)
    a.append('c')
    print(a)
