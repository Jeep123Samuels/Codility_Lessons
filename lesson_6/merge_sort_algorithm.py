"""Merge Sort Algorithm."""


def merge(left_array, right_array):
    """Merge the two arrays in order."""
    result_array = []

    while left_array and right_array:
        if left_array[0] <= right_array[0]:
            result_array.append(left_array[0])
            left_array.pop(0)
        else:
            result_array.append(right_array[0])
            right_array.pop(0)
    return result_array + left_array if left_array else result_array + right_array


def halve_sort(A):
    """Halve given array in equal parts, until length 1, and then re-assemble in order."""
    len_a = len(A)
    if len_a <= 1:
        return A

    left_array = halve_sort(A[:len_a//2])
    right_array = halve_sort(A[len_a//2:])

    return merge(left_array, right_array)


def merge_sort(A):  # noqa
    merge(halve_sort(A))


if __name__ == "__main__":
    a = [4, 1, 2, 3]
    # [4, 1, 2, 3]
    print(halve_sort(a))

    # print(a[:len(a)/2])
