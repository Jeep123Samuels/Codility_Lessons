"""Main script for binary_gaps.py"""


# For example, given N = 1041 the function should return 5,
# because N has binary representation 10000010001 and so its longest binary gap is of length 5.
#
# Assume that:
#
# N is an integer within the range [1..2,147,483,647].
# Complexity:
#
# expected worst-case time complexity is O(log(N));
# expected worst-case space complexity is O(1).
import random


def solution(integer_str):
    """Returns maximum binary gap for a given binary string."""
    gaps = [len(x) for x in integer_str.rstrip('0').lstrip('0').split('1')]
    return max(gaps) if gaps else 0


if __name__ == "__main__":
    for _ in range(10):
        i = random.randint(200, 647)
        binary_str = str(bin(i))[2:]
        print('i : {0}'.format(i))
        print('i binary : {0}'.format(binary_str))
        print('solution: {0}\n'.format(solution(binary_str)))
