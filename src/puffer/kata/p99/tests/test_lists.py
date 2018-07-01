import pytest
from src.puffer.kata.p99.lists import find_last, find_last_diy, find_last_but_one


@pytest.mark.parametrize("func", [find_last, find_last_diy])
def test_find_last(func):
    """
    P01 (*) Find the last element of a list.
    Example:
    ?- my_last(X,[a,b,c,d]).
    X = d
    """
    ints = [1, 2, 3, 4]
    chars = ['a', 'b', 'c', 'd']

    assert func(ints) == 4
    assert func(chars) == 'd'


def test_find_last_but_one():
    """
    P02 (*) Find the last but one element of a list.
    (zweitletztes Element, l'avant-dernier élément)
    """
    ints = [1, 2, 3, 4]
    chars = ['a', 'b', 'c', 'd']

    assert find_last_but_one(ints) == 3
    assert find_last_but_one(chars) == 'c'
