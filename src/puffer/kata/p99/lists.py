from typing import List


def find_last_pythonic(given: List):
    return given[-1]


def find_last(given: List):
    def _find(_next: List):
        if len(_next) == 1:
            return _next.pop()
        else:
            return _find(_next[1:])

    return _find(given)


def find_last_but_one(given: List):
    copy = given.copy()
    copy.pop()
    return find_last_pythonic(copy)


def element_at_pythonic(given: List, i: int):
    return given[i-1]


def element_at(given: List, i: int):
    for j, elem in enumerate(given):
        if j+1 == i:
            return elem

    raise ValueError


def num_of_elements_pythonic(given: List):
    return len(given)


def num_of_elements(given: List):
    n = 0
    for _ in given:
        n += 1
    return n


def reverse(given: List):
    return list(reversed(given))


def reverse_diy(given: List):
    result = [None] * len(given)
    for i, elem in enumerate(given):
        result[-(i+1)] = elem

    return result


def is_palindrome(given: List):
    half = int(len(given) / 2)
    for i in range(0,half):
        if given[i] != given[-(i+1)]:
            return False
    return True


def flatten(given: List):
    result = []
    for elem in given:
        if isinstance(elem, List):
            for _elem in flatten(elem):
                result.append(_elem)
        else:
            result.append(elem)

    return result


def compress(given: List):
    from functools import reduce
    return reduce(lambda x, y: x if x and x[-1] == y else x + [y], given, [])


def pack(given: List):
    def _append(alist: List, elem) -> List:
        alist[-1].append(elem)
        return alist

    def _new(alist: List, elem) -> List:
        alist.append([elem])
        return alist

    from functools import reduce
    return reduce(lambda x, y: _append(x, y) if x and x[-1] and x[-1][-1] == y else _new(x, y), given, [])
