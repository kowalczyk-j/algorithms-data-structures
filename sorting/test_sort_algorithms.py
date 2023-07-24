from sort_algorithms import selection_sort, quicksort, bubble_sort, merge_sort
from read_file import read_file
import sys

sys.setrecursionlimit(50000)


pan_tadeusz = read_file("pan-tadeusz-unix.txt")


# SELECTION SORT

def test_selection_sort_numbers():
    a = [4, 10, 2, -10, 2, 1, -2]
    assert [-10, -2, 1, 2, 2, 4, 10] == selection_sort(a)


def test_selection_sort_letters():
    a = ["a", "y", "b", "x"]
    assert ["a", "b", "x", "y"] == selection_sort(a)


def test_selection_sort_words():
    a = ["algorytmy", "i", "struktury", "danych"]
    assert ["algorytmy", "danych", "i", "struktury"] == selection_sort(a)


def test_selection_sort_benchmark_1000(benchmark):
    benchmark(selection_sort, pan_tadeusz[:1000])


def test_selection_sort_benchmark_2000(benchmark):
    benchmark(selection_sort, pan_tadeusz[:2000])


def test_selection_sort_benchmark_5000(benchmark):
    benchmark(selection_sort, pan_tadeusz[:5000])


def test_selection_sort_benchmark_10000(benchmark):
    benchmark(selection_sort, pan_tadeusz[:10000])

# QUICKSORT


def test_quicksort_numbers():
    a = [4, 10, 2, -10, 2, 1, -2]
    quicksort(a, 0, len(a)-1)
    assert [-10, -2, 1, 2, 2, 4, 10] == a


def test_quicksort_letters():
    a = ["a", "y", "b", "x"]
    quicksort(a, 0, len(a)-1)
    assert ["a", "b", "x", "y"] == a


def test_quicksort_words():
    a = ["algorytmy", "i", "struktury", "danych"]
    quicksort(a, 0, len(a)-1)
    assert ["algorytmy", "danych", "i", "struktury"] == a


def test_quicksort_benchmark_1000(benchmark):
    benchmark(quicksort, pan_tadeusz[:1000], 0, 999)


def test_quicksort_benchmark_2000(benchmark):
    benchmark(quicksort, pan_tadeusz[:2000], 0, 1999)


def test_quicksort_benchmark_5000(benchmark):
    benchmark(quicksort, pan_tadeusz[:5000], 0, 4999)


def test_quicksort_benchmark_10000(benchmark):
    benchmark(quicksort, pan_tadeusz[:10000], 0, 9999)


# BUBBLE SORT

def test_bubble_sort_numbers():
    a = [4, 10, 2, -10, 2, 1, -2]
    assert [-10, -2, 1, 2, 2, 4, 10] == bubble_sort(a)


def test_bubble_sort_letters():
    a = ["a", "y", "b", "x"]
    assert ["a", "b", "x", "y"] == bubble_sort(a)


def test_bubble_sort_words():
    a = ["algorytmy", "i", "struktury", "danych"]
    assert ["algorytmy", "danych", "i", "struktury"] == bubble_sort(a)


def test_bubble_sort_benchmark_1000(benchmark):
    benchmark(bubble_sort, pan_tadeusz[:1000])


def test_bubble_sort_benchmark_2000(benchmark):
    benchmark(bubble_sort, pan_tadeusz[:2000])


def test_bubble_sort_benchmark_5000(benchmark):
    benchmark(bubble_sort, pan_tadeusz[:5000])


def test_bubble_sort_benchmark_10000(benchmark):
    benchmark(bubble_sort, pan_tadeusz[:10000])

# MERGE SORT


def test_merge_sort_numbers():
    a = [4, 10, 2, -10, 2, 1, -2]
    assert [-10, -2, 1, 2, 2, 4, 10] == merge_sort(a)


def test_merge_sort_letters():
    a = ["a", "y", "b", "x"]
    assert ["a", "b", "x", "y"] == merge_sort(a)


def test_merge_sort_words():
    a = ["algorytmy", "i", "struktury", "danych"]
    assert ["algorytmy", "danych", "i", "struktury"] == merge_sort(a)


def test_merge_sort_benchmark_1000(benchmark):
    benchmark(merge_sort, pan_tadeusz[:1000])


def test_merge_sort_benchmark_2000(benchmark):
    benchmark(merge_sort, pan_tadeusz[:2000])


def test_merge_sort_benchmark_5000(benchmark):
    benchmark(merge_sort, pan_tadeusz[:5000])


def test_merge_sort_benchmark_10000(benchmark):
    benchmark(merge_sort, pan_tadeusz[:10000])
