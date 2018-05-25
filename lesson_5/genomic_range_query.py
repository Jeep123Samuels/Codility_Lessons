"""Main script for genomic_range_query.py"""

# A DNA sequence can be represented as a string consisting of the letters
# A, C, G and T, which correspond to the types of successive nucleotides in the sequence.
# Each nucleotide has an impact factor, which is an integer.
# Nucleotides of types A, C, G and T have impact factors of 1, 2, 3 and 4, respectively.
# You are going to answer several queries of the form:
# What is the minimal impact factor of nucleotides contained
# in a particular part of the given DNA sequence?
#
# The DNA sequence is given as a non-empty string S = S[0]S[1]...S[N-1] consisting of N characters.
# There are M queries, which are given in non-empty arrays P and Q, each consisting of M integers.
# The K-th query (0 <= K < M) requires you to find the minimal impact factor of nucleotides contained
# in the DNA sequence between positions P[K] and Q[K] (inclusive).
#
# For example, consider string S = CAGCCTA and arrays P, Q such that:
#
#     P[0] = 2    Q[0] = 4
#     P[1] = 5    Q[1] = 5
#     P[2] = 0    Q[2] = 6
# The answers to these M = 3 queries are as follows:
#
# The part of the DNA between positions 2 and 4 contains nucleotides G and C (twice),
# whose impact factors are 3 and 2 respectively, so the answer is 2.
# The part between positions 5 and 5 contains a single nucleotide T,
# whose impact factor is 4, so the answer is 4.
# The part between positions 0 and 6 (the whole string) contains all nucleotides,
# in particular nucleotide A whose impact factor is 1, so the answer is 1.
#
# Write a function:
#
# def solution(S, P, Q)
#
# that, given a non-empty string S consisting of N characters and
# two non-empty arrays P and Q consisting of M integers,
# returns an array consisting of M integers specifying the consecutive answers to all queries.
#
# The sequence should be returned as:
#
# a Results structure (in C), or
# a vector of integers (in C++), or
# a Results record (in Pascal), or
# an array of integers (in any other programming language).
# For example, given the string S = CAGCCTA and arrays P, Q such that:
#
#     P[0] = 2    Q[0] = 4
#     P[1] = 5    Q[1] = 5
#     P[2] = 0    Q[2] = 6
# the function should return the values [2, 4, 1], as explained above.
#
# Assume that:
#
# N is an integer within the range [1..100,000];
# M is an integer within the range [1..50,000];
# each element of arrays P, Q is an integer within the range [0..N - 1];
# P[K] <= Q[K], where 0 <= K < M;
# string S consists only of upper-case English letters A, C, G, T.
# Complexity:
#
# expected worst-case time complexity is O(N+M);
# expected worst-case space complexity is O(N) (not counting the storage required for input arguments).


def solution(S, P, Q):
    """
    Returns the least factor DNA-character in a given range.

    First:
        Step thru the given string creating a last-seen key-value array.
        E.g: 'T': [contains the integers of the last seen index]

    Second:
        Step thru the given ranges and then comparing the ranges with the
        last seen array from the dictionary.
    """
    result = []
    DNA_len = len(S)
    next_nucl = {
        'A': [-1] * DNA_len,
        'C': [-1] * DNA_len,
        'G': [-1] * DNA_len,
        'T': [-1] * DNA_len,
    }

    # Mark the first occurrence in the DNA string.
    next_nucl[S[0]][0] = 0
    # Step thru the given  DNA string building a last seen key-value pair.
    for index in range(1, DNA_len, 1):
        # Mark current position with last seen position.
        # This will cater for the case of the character not appearing.
        # This also avoids using a if to check which needs to be assigned
        # the last-seen position and which should not.
        next_nucl['A'][index] = next_nucl['A'][index - 1]
        next_nucl['C'][index] = next_nucl['C'][index - 1]
        next_nucl['G'][index] = next_nucl['G'][index - 1]
        next_nucl['T'][index] = next_nucl['T'][index - 1]
        # Now we set actual current character's position to the current.
        next_nucl[S[index]][index] = index

    for index in range(0, len(P)):
        # Check if the position is filled and then if the position at that index falls
        # in the range of the P[i] and Q[i] query ===> P[i] <= filled position <= Q[i]
        # Check first if the upper_limit query have seen the character, then
        # check if the last_seen value is greater then the lower_limit which will mean,
        # the character is in that range, other wise continue.
        if next_nucl['A'][Q[index]] != -1 and next_nucl['A'][Q[index]] >= P[index]:
            result.append(1)
        elif next_nucl['C'][Q[index]] != -1 and next_nucl['C'][Q[index]] >= P[index]:
            result.append(2)
        elif next_nucl['G'][Q[index]] != -1 and next_nucl['G'][Q[index]] >= P[index]:
            result.append(3)
        else:
            result.append(4)

    return result


if __name__ == "__main__":
    solution('CAGCCTA', [2, 5, 0], [4, 5, 6])
