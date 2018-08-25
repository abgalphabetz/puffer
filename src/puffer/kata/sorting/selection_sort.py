from collections import Sequence


def selection_sort(given: Sequence):
    print()
    given_list = list(given)
    size = len(given_list)
    for i in range(0, size):
        k = i
        print(f"{given_list}")
        for j in range(i, size):
            if given_list[j] < given_list[k]:
                k = j
        given_list[i], given_list[k] = given_list[k], given_list[i]

    return given_list
