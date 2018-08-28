from typing import Sequence


def quick_sort(given: Sequence):
    if len(given) <= 1:
        return given

    pivot = given[0]
    left, right = [], []

    for i in range(1, len(given)):
        if given[i] < pivot:
            left.append(given[i])
        else:
            right.append(given[i])

    lsorted = quick_sort(left)
    rsorted = quick_sort(right)

    print(given, " -> ", lsorted, pivot, rsorted)
    return lsorted + [pivot] + rsorted


def quick_sort_inplace(given: Sequence):
    if len(given) <= 1:
        return given

    given_list = list(given)
    pivot = given_list[0]
    left, right = 1, len(given_list) - 1

    while left <= right:
        if given_list[left] >= pivot >= given_list[right]:
            given_list[left], given_list[right] = given_list[right], given_list[left]
            left += 1
            right -= 1
        else:
            if given_list[left] < pivot:
                left += 1

            if given_list[right] > pivot:
                right -= 1

    if right > 0:
        given_list[0], given_list[right] = given_list[right], given_list[0]

    print(given_list)

    return quick_sort_inplace(given_list[:right]) + [pivot] + quick_sort_inplace(given_list[right + 1:])
