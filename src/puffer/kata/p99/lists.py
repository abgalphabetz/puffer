from typing import List, Set, Sequence


def find_last_pythonic(given: Sequence):
    return given[-1]


def find_last(given: Sequence):
    def _find(_next: Sequence):
        if len(_next) == 1:
            return _next[-1]
        else:
            return _find(_next[1:])

    return _find(given)


def find_last_but_one(given: Sequence):
    return find_last_pythonic(given[:-1])


def element_at_pythonic(given: Sequence, i: int):
    return given[i - 1]


def element_at(given: Sequence, i: int):
    for j, elem in enumerate(given):
        if j + 1 == i:
            return elem

    raise ValueError


def num_of_elements_pythonic(given: Sequence):
    return len(given)


def num_of_elements(given: Sequence):
    n = 0
    for _ in given:
        n += 1
    return n


def reverse_pythonic(given: Sequence):
    return list(reversed(given))


def reverse(given: Sequence):
    result = [None] * len(given)
    for i, elem in enumerate(given):
        result[-(i + 1)] = elem

    return result


def is_palindrome(given: Sequence):
    half = int(len(given) / 2)
    for i in range(0, half):
        if given[i] != given[-(i + 1)]:
            return False
    return True


def flatten(given: Sequence):
    result = []
    for elem in given:
        if isinstance(elem, List):
            for _elem in flatten(elem):
                result.append(_elem)
        else:
            result.append(elem)

    return result


def compress_pythonic(given: Sequence):
    from functools import reduce
    return reduce(lambda x, y: x if x and x[-1] == y else x + [y], given, [])


def compress(given: Sequence):
    def _compress(src: Sequence, dest: Sequence):
        if not src:
            return dest

        elem, tail = src[0], src[1:]
        if not dest or elem != dest[-1]:
            dest.append(elem)

        return _compress(tail, dest)

    return _compress(given, [])


def _pack_append(_list: Sequence[List], elem) -> List:
    _list[-1].append(elem)
    return _list


def _pack_new(_list: Sequence[List], elem) -> List:
    _list.append([elem])
    return _list


def pack_pythonic(given: Sequence):
    from functools import reduce
    return reduce(lambda x, y: _pack_append(x, y) if x and x[-1] and x[-1][-1] == y else _pack_new(x, y), given, [])


def pack(given: Sequence):
    def _pack(src: Sequence, dest: Sequence):
        if not src:
            return dest

        elem, tail = src[0], src[1:]
        if dest and dest[-1] and dest[-1][-1] == elem:
            return _pack(tail, _pack_append(dest, elem))
        return _pack(tail, _pack_new(dest, elem))

    return _pack(given, [])


def encode_pythonic(given: Sequence):
    return list(map(lambda l: [len(l), l[0]], pack(given)))


def encode(given: Sequence):
    result = []
    for l in pack(given):
        result.append([len(l), l[0]])

    return result


def encode_modified_pythonic(given: Sequence):
    return [x if x[0] > 1 else x[1] for x in encode_pythonic(given)]


def encode_modified(given: Sequence):
    result = []
    for l in pack(given):
        size = len(l)
        result.append(l[0] if size == 1 else [size, l[0]])

    return result


def decode_pythonic(given: Sequence):
    def _decode(elem) -> List:
        if isinstance(elem, List):
            return [elem[1]] * elem[0]
        else:
            return [elem]

    from functools import reduce
    return reduce(lambda x, y: x + _decode(y), given, [])


def decode(given: Sequence):
    def _decode(elem) -> List:
        if isinstance(elem, List):
            return [elem[1]] * elem[0]
        else:
            return [elem]

    result = []
    for elem in given:
        result += _decode(elem)
    return result


def encode_direct_pythonic(given: Sequence):
    def _encode_direct(x, y):
        if not x or x[-1][-1] != y:
            return x + [[1, y]]
        else:
            x[-1][0] += 1
            return x

    from functools import reduce
    encoded = reduce(_encode_direct, given, [])
    return list(map(lambda x: x if x[0] > 1 else x[1], encoded))


def duplicate_pythonic(given: Sequence, times=2):
    from functools import reduce
    return reduce(lambda x, y: x + [y] * times, given, [])


def duplicate(given: Sequence, times=2):
    result = []
    for elem in given:
        result += [elem] * times
    return result


def drop_pythonic(given: Sequence, nth: int):
    return [elem for i, elem in enumerate(given) if (i + 1) % nth != 0]


def drop(given: Sequence, nth: int):
    result = []
    for i, elem in enumerate(given):
        if (i + 1) % nth != 0:
            result.append(elem)
        else:
            continue
    return result


def split_pythonic(given: Sequence, n: int):
    return list(given[:n]), list(given[n:])


def split(given: Sequence, n: int):
    list1, list2 = [], []
    for i, elem in enumerate(given):
        (list1 if i < n else list2).append(elem)
    return list1, list2


def slice_pythonic(given: Sequence, start: int, end: int):
    return list(given[start - 1:end])


def slice_diy(given: Sequence, start: int, end: int):
    return [elem for i, elem in enumerate(given) if start - 1 <= i < end]


def rotate_pythonic(given: Sequence, n: int):
    return list(given[n:]) + list(given[:n])


def rotate(given: Sequence, n: int):
    _n = n if n > 0 else len(given) + n
    ls = split(given, _n)
    return ls[1] + ls[0]


def remove_at_pythonic(given: Sequence, kth: int):
    return [x for i, x in enumerate(given) if i != kth - 1]


def remove_at(given: Sequence, kth: int):
    ls = split(given, kth - 1)
    return ls[0] + ls[1][1:]


def insert_at_pythonic(elem, given: Sequence, kth: int):
    return list(given[:kth - 1]) + [elem] + list(given[kth - 1:])


def insert_at(elem, given: Sequence, kth: int):
    ls = split(given, kth - 1)
    from itertools import chain
    return list(chain(ls[0], [elem], ls[1]))


def range_pythonic(start: int, end: int):
    return list(range(start, end + 1))


def rnd_select(given: Sequence, no_of_elements: int):
    import random
    return random.sample(given, no_of_elements)


def rnd_permutation(given: Sequence):
    return rnd_select(given, len(given))


def combination(given: Sequence, r: int):
    def _select(_given: Sequence, _r):
        if r <= 0 or not _given:
            return [[]]

        list_size = len(_given)
        if list_size < _r:
            return [[]]

        if _r == 1:
            return [[x] for x in _given]
        elif list_size == _r:
            return [_given]
        else:
            head, tail = _given[0], _given[1:]
            return [[head] + list(s) for s in _select(tail, _r - 1)] + _select(tail, _r)

    return _select(given, r)


def _split(_given: Sequence, n: int) -> List:
    selected = combination(_given, n)
    result = [[s, list(set(_given) - set(s))] for s in selected]
    return result


def group3(given: Sequence, groups_of_3: Sequence):
    if len(groups_of_3) != 3 or len(given) != sum(groups_of_3):
        raise ValueError

    result = []
    splits = _split(given, groups_of_3[0])
    for s in splits:
        s2 = _split(s[1], groups_of_3[1])
        result.append([[s[0]] + ss for ss in s2])

    flattened = [r[0] for r in result]
    return flattened


def group(given: Sequence, groups: Sequence):
    def _group(_given: Sequence, _groups: Sequence):
        if not _groups:
            return [[[]]]

        head, tail = _groups[0], _groups[1:]
        splits = _split(_given, head)
        m = list(map(lambda s: [[s[0]] + g for g in group(s[-1], tail)], splits))
        result = m
        return result

    if len(given) != sum(groups):
        raise ValueError
    elif len(groups) == 1:
        return [[given]]

    grouped = _group(given, groups)
    flattened = [g[0] for g in grouped]
    return flattened


def lsort_pythonic(given: Sequence):
    return sorted(given, key=lambda x: len(x))


def lfsort_pythonic(given: Sequence):
    l = [len(x) for x in given]
    f = [(z[0], z[1]) for z in zip(given, l)]

    s = sorted(f, key=lambda item: -item[1])
    return [i for i, f in s]
