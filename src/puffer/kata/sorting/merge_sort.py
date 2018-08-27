from collections import Sequence


def merge_sort(given: Sequence):
    given_list = list(given)
    size = len(given_list)

    if size == 1:
        return given_list

    k = size // 2
    left = merge_sort(given_list[0:k])
    right = merge_sort(given_list[k:])

    tmp = []
    lnext, lsize = 0, len(left)
    rnext, rsize = 0, len(right)
    for i in range(0, lsize+rsize):
        if lnext == lsize and rnext < rsize:
            tmp.extend(right[rnext:])
            break
        elif rnext == rsize and lnext < lsize:
            tmp.extend(left[lnext:])
            break

        if left[lnext] <= right[rnext]:
            tmp.append(left[lnext])
            lnext += 1
        else:
            tmp.append(right[rnext])
            rnext += 1

    return tmp

