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
