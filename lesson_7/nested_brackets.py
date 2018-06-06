"""Main script for nested_brackets.py"""

# A string S consisting of N characters is considered to be properly
# nested if any of the following conditions is true:
#
# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.
#
# Write a function:
#
# def solution(S)
#
# that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.
#
# For example, given S = "{[()()]}", the function should return 1 and
# given S = "([)()]", the function should return 0, as explained above.
#
# Assume that:
#
# N is an integer within the range [0..200,000];
# string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
# Complexity:
#
# expected worst-case time complexity is O(N);
# expected worst-case space complexity is O(N) (not counting the storage required for input arguments).


def solution(S):
    """Returns validated result on a string for nested brackets."""
    N = len(S)
    if N % 2 != 0:
        return 0
    if N == 0:
        return 1
    left_brackets = list()
    valid_characters = '[]{}()'
    left_brackets_chars = '{[('
    right_brackets_chars = ']})'

    for x in S:
        # Check not valid character input.
        if x not in valid_characters:
            return 0
        # insert left_brackets in half array
        if x in left_brackets_chars:
            left_brackets.append(x)

        elif x in right_brackets_chars:
            if (
                (not left_brackets) or
                (left_brackets[-1] == '[' and x != ']') or
                (left_brackets[-1] == '{' and x != '}') or
                (left_brackets[-1] == '(' and x != ')')
            ):
                return 0
            left_brackets.pop()
    if left_brackets:
        return 0
    return 1

if __name__ == "__main__":
    H = [8, 8, 5, 7, 9, 8, 7, 4, 8]
    a = list()
    a.append('a')
    print(a)
    a.append('b')
    print(a)
    a.append('c')
    print(a)
