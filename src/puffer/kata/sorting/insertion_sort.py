from collections import Sequence


def insertion_sort(given: Sequence):
    given_list = list(given)
    size = len(given_list)

    print()
    for i in range(1, size):
        print(given_list)
        k = i
        for j in range(0, i):
            if given_list[j] > given_list[i]:
                k = j
                break
        if k == i:
            continue

        given_list[k], given_list[k+1:i+1] = given_list[i], given_list[k:i]

    return given_list


