from collections import Sequence
from typing import List


def merge_sort(given: Sequence):
    given_list = list(given)
    size = len(given_list)

    if size == 1:
        return given_list

    k = size // 2
    left = merge_sort(given_list[0:k])
    right = merge_sort(given_list[k:])

    return _merge_sorted_lists(left, right)


def _merge_sorted_lists(left: List, right: List):
    tmp = []
    lnext = 0
    rnext = 0
    while lnext < len(left) and rnext < len(right):
        if left[lnext] <= right[rnext]:
            tmp.append(left[lnext])
            lnext += 1
        else:
            tmp.append(right[rnext])
            rnext += 1

    if rnext < len(right):
        tmp.extend(right[rnext:])

    if lnext < len(left):
        tmp.extend(left[lnext:])

    return tmp
