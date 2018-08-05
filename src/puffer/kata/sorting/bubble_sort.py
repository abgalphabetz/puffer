from collections import Sequence


def bubble_sort(given: Sequence):
    print()
    given_list = list(given)
    size = len(given_list)
    for i in range(1, size):
        print(f"{given_list}")
        unsorted_elements = size - i
        for j in range(0, unsorted_elements):
            m = given_list[j]
            n = given_list[j + 1]
            if m > n:
                given_list[j], given_list[j + 1] = n, m

    return given_list
