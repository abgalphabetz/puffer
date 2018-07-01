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
    given.pop()
    return find_last(given)
