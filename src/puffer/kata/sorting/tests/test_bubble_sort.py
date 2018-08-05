import pytest

from src.puffer.kata.sorting.bubble_sort import bubble_sort


@pytest.mark.parametrize(("given", "expected"), [
    ((1, 4, 3, 2), [1, 2, 3, 4]),
    ((4, 3, 2, 1), [1, 2, 3, 4]),
    ((1, 2, 3, 4), [1, 2, 3, 4]),
])
def test_bubble_sort(given, expected):
    assert expected == bubble_sort(given)
