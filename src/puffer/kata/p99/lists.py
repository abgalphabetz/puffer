from typing import List


def find_last(given: List):
    return given[-1]


def find_last_diy(given: List):
    def _find(_next: List):
        if len(_next) == 1:
            return _next.pop()
        else:
            return _find(_next[1:])

    return _find(given)


def find_last_but_one(given: List):
    return find_last(given.copy().pop())


def element_at(given: List, i: int):
    return given[i-1]


def element_at_diy(given: List, i: int):
    for j, elem in enumerate(given):
        if j+1 == i:
            return elem

    raise ValueError


def num_of_elements(given: List):
    return len(given)


def num_of_elements_diy(given: List):
    n = 0
    for _ in given:
        n += 1
    return n


