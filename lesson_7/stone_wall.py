"""Main script for stone_wall.py"""

# You are going to build a stone wall.
# The wall should be straight and N meters long, and its thickness should be constant;
# however, it should have different heights in different places.
# The height of the wall is specified by an array H of N positive integers.
# H[I] is the height of the wall from I to I+1 meters to the right of its left end.
# In particular, H[0] is the height of the wall's left end and H[N−1] is the height of the wall's right end.
#
# The wall should be built of cuboid stone blocks (that is, all sides of such blocks are rectangular).
# Your task is to compute the minimum number of blocks needed to build the wall.
#
# Write a function:
#
# def solution(H)
#
# that, given an array H of N positive integers specifying the height of the wall,
# returns the minimum number of blocks needed to build it.
#
# For example, given array H containing N = 9 integers:
#
#   H[0] = 8    H[1] = 8    H[2] = 5
#   H[3] = 7    H[4] = 9    H[5] = 8
#   H[6] = 7    H[7] = 4    H[8] = 8
# the function should return 7. The figure shows one possible arrangement of seven blocks.
#
#
#
# Assume that:
#
# N is an integer within the range [1..100,000];
# each element of array H is an integer within the range [1..1,000,000,000].
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N) (not counting the storage required for input arguments).



def solution(A):
    """Returns the minimum stones needed to build wall."""
    N = len(H)
    stones = 0
    stack = [0] * N
    stack_num = 0

    for i in range(N):
        while stack_num > 0 and stack[stack_num-1] > H[i]:
            stack_num -= 1
        if stack_num > 0 and stack[stack_num-1] == H[i]:
            pass
        else:
            stones += 1
            stack[stack_num] = H[i]
            stack_num += 1
    return stones


class Queue(object):
    head = None
    tail = None
    queue = None
    N = None

    def __init__(self, N):
        self.N = N
        self.queue = [0] * N
        self.head = self.tail = 0

    def pop(self):
        self.head += 1

    def push(self, value):
        self.queue[self.tail] = value
        self.tail += 1

    def empty(self):
        return self.head == self.tail

    def size(self):
        return (self.tail - self.head + self.N) % self.N

if __name__ == "__main__":
    H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
