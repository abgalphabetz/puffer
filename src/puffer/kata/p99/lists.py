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
    return given[i - 1]


def element_at(given: List, i: int):
    for j, elem in enumerate(given):
        if j + 1 == i:
            return elem

    raise ValueError


def num_of_elements_pythonic(given: List):
    return len(given)


def num_of_elements(given: List):
    n = 0
    for _ in given:
        n += 1
    return n


def reverse_pythonic(given: List):
    return list(reversed(given))


def reverse(given: List):
    result = [None] * len(given)
    for i, elem in enumerate(given):
        result[-(i + 1)] = elem

    return result


def is_palindrome(given: List):
    half = int(len(given) / 2)
    for i in range(0, half):
        if given[i] != given[-(i + 1)]:
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


def compress_pythonic(given: List):
    from functools import reduce
    return reduce(lambda x, y: x if x and x[-1] == y else x + [y], given, [])


def compress(given: List):
    def _compress(src: List, dest: List):
        if not src:
            return dest

        elem = src.pop(0)
        if not dest or elem != dest[-1]:
            dest.append(elem)

        return _compress(src, dest)

    compress = _compress(given.copy(), [])
    return compress


def _pack_append(_list: List[List], elem) -> List:
    _list[-1].append(elem)
    return _list


def _pack_new(_list: List[List], elem) -> List:
    _list.append([elem])
    return _list


def pack_pythonic(given: List):
    from functools import reduce
    return reduce(lambda x, y: _pack_append(x, y) if x and x[-1] and x[-1][-1] == y else _pack_new(x, y), given, [])


def pack(given: List):
    def _pack(src: List, dest: List):
        if not src:
            return dest

        elem = src.pop(0)
        if dest and dest[-1] and dest[-1][-1] == elem:
            return _pack(src, _pack_append(dest, elem))
        return _pack(src, _pack_new(dest, elem))

    return _pack(given.copy(), [])


def encode_pythonic(given: List):
    return list(map(lambda l: [len(l), l[0]], pack(given)))


def encode(given: List):
    result = []
    for l in pack(given):
        result.append([len(l), l[0]])

    return result


def encode_modified_pythonic(given: List):
    return [x if x[0] > 1 else x[1] for x in encode_pythonic(given)]


def encode_modified(given: List):
    result = []
    for l in pack(given):
        size = len(l)
        result.append(l[0] if size == 1 else [size, l[0]])

    return result


def decode_pythonic(given: List):
    def _decode(elem) -> List:
        if isinstance(elem, List):
            return [elem[1]] * elem[0]
        else:
            return [elem]

    from functools import reduce
    return reduce(lambda x, y: x + _decode(y), given, [])


def decode(given: List):
    def _decode(elem) -> List:
        if isinstance(elem, List):
            return [elem[1]] * elem[0]
        else:
            return [elem]

    result = []
    for elem in given:
        result += _decode(elem)
    return result


def encode_direct_pythonic(given: List):
    def _encode_direct(x, y):
        if not x or x[-1][-1] != y:
            return x + [[1, y]]
        else:
            x[-1][0] += 1
            return x

    from functools import reduce
    encoded = reduce(_encode_direct, given, [])
    return list(map(lambda x: x if x[0] > 1 else x[1], encoded))


def duplicate_pythonic(given: List, times=2):
    from functools import reduce
    return reduce(lambda x, y: x + [y] * times, given, [])


def duplicate(given: List, times=2):
    result = []
    for elem in given:
        result += [elem] * times
    return result


def drop_pythonic(given: List, nth: int):
    return [elem for i, elem in enumerate(given) if (i+1) % nth != 0]


def drop(given: List, nth: int):
    result = []
    for i, elem in enumerate(given):
        if (i+1) % nth != 0:
            result.append(elem)
        else:
            continue
    return result


def split_pythonic(given: List, n: int):
    return given[:n], given[n:]


def split(given: List, n: int):
    list1, list2 = [], []
    for i, elem in enumerate(given):
        (list1 if i < n else list2).append(elem)
    return list1, list2


def slice_pythonic(given: List, start: int, end: int):
    return given[start-1:end]


def slice_diy(given: List, start: int, end: int):
    return [elem for i, elem in enumerate(given) if start - 1 <= i < end]


def rotate_pythonic(given: List, n: int):
    return given[n:] + given[:n]


def rotate(given: List, n: int):
    _n = n if n > 0 else len(given) + n
    ls = split(given, _n)
    return ls[1] + ls[0]


def remove_at_pythonic(given: List, kth: int):
    return [x for i, x in enumerate(given) if i != kth-1]


def remove_at(given: List, kth: int):
    ls = split(given, kth-1)
    return ls[0] + ls[1][1:]


def insert_at_pythonic(elem, given: List, kth: int):
    return given[:kth-1] + [elem] + given[kth-1:]


def insert_at(elem, given: List, kth: int):
    ls = split(given, kth-1)
    from itertools import chain
    return list(chain(ls[0], [elem], ls[1]))
