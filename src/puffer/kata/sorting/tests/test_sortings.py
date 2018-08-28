import pytest

from src.puffer.kata.sorting.insertion_sort import insertion_sort
from src.puffer.kata.sorting.merge_sort import merge_sort
from src.puffer.kata.sorting.quick_sort import quick_sort, quick_sort_inplace
from src.puffer.kata.sorting.selection_sort import selection_sort
from src.puffer.kata.sorting.bubble_sort import bubble_sort


@pytest.mark.parametrize("sorting_func", [
    bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, quick_sort_inplace
])
def test_sorting_function(sorting_func):
    ints1 = (1, 4, 3, 2, 2, 5, 9, 8, 7)
    ints2 = (4, 1, 3, 2, 2, 5, 9, 8, 7)

    assert sorted(ints1) == sorting_func(ints1)
    assert sorted(ints2) == sorting_func(ints2)
