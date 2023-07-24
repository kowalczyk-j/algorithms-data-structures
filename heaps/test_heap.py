from heap import BinaryHeap, ThreearyHeap, FouraryHeap
from random import sample
import pytest


INTEGERS = sample(range(1, 300000), 100000)


@pytest.fixture
def bheap():
    bheap = BinaryHeap()
    for num in INTEGERS:
        bheap.push(num)
    return bheap


@pytest.fixture
def theap():
    theap = ThreearyHeap()
    for num in INTEGERS:
        theap.push(num)
    return theap


@pytest.fixture
def fheap():
    fheap = FouraryHeap()
    for num in INTEGERS:
        fheap.push(num)
    return fheap


def add_n_elements(heap, n):
    for number in INTEGERS[:n]:
        heap.push(number)


def pop_n_elements(heap, n):
    for _ in range(n):
        heap.pop()


def test_empty_heaps():
    bheap = BinaryHeap()
    theap = ThreearyHeap()
    fheap = FouraryHeap()
    assert len(bheap) == 0
    assert len(theap) == 0
    assert len(fheap) == 0


def test_binary_heap_push():
    bheap = BinaryHeap()
    nums = [5, 15, -5, 2, 3, 25]
    for num in nums:
        bheap.push(num)
    assert len(bheap) == 6
    assert bheap.peek() == -5


def test_threeary_heap_push():
    theap = ThreearyHeap()
    nums = [8, 21, 52, 52, 8, 52, 152]
    for num in nums:
        theap.push(num)
    assert len(theap) == 7
    assert theap.peek() == 8


def test_fourary_heap_push():
    fheap = FouraryHeap()
    nums = [-123, -53, -512, -12, 8, -21, -21]
    for num in nums:
        fheap.push(num)
    assert len(fheap) == 7
    assert fheap.peek() == -512


def test_empty_heap_pop():
    bheap = BinaryHeap()
    theap = ThreearyHeap()
    fheap = FouraryHeap()
    with pytest.raises(ValueError):
        bheap.pop()
        theap.pop()
        fheap.pop()


def test_binary_heap_pop():
    bheap = BinaryHeap()
    nums = [5, 6, 0, 2, 3, 10, 8, 9, 4, 1, 11, 7]
    for num in nums:
        bheap.push(num)
    expected_vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, None]
    for i in range(len(expected_vals)-1):
        assert bheap.pop() == expected_vals[i]
        assert len(bheap) == expected_vals[-(i+2)]
        assert bheap.peek() == expected_vals[i+1]


def test_threeary_heap_pop():
    theap = ThreearyHeap()
    nums = [8, 3, 5, 6, 7, 1, 2, 10, 11, 4, 9, 0]
    for num in nums:
        theap.push(num)
    expected_vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, None]
    for i in range(len(expected_vals)-1):
        assert theap.pop() == expected_vals[i]
        assert len(theap) == expected_vals[-(i+2)]
        assert theap.peek() == expected_vals[i+1]


def test_fourary_heap_pop():
    fheap = FouraryHeap()
    nums = [11, 10, 9, 8, 7, 6, 5, 4, 0, 1, 2, 3]
    for num in nums:
        fheap.push(num)
    expected_vals = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, None]
    for i in range(len(expected_vals)-1):
        assert fheap.pop() == expected_vals[i]
        assert len(fheap) == expected_vals[-(i+2)]
        assert fheap.peek() == expected_vals[i+1]


# BINARY HEAP
def test_add_bheap_1000(benchmark):
    bheap = BinaryHeap()
    benchmark.pedantic(add_n_elements, args=(bheap, 1000))


def test_add_bheap_2000(benchmark):
    bheap = BinaryHeap()
    benchmark.pedantic(add_n_elements, args=(bheap, 2000))


def test_add_bheap_5000(benchmark):
    bheap = BinaryHeap()
    benchmark.pedantic(add_n_elements, args=(bheap, 5000))


def test_add_bheap_7000(benchmark):
    bheap = BinaryHeap()
    benchmark.pedantic(add_n_elements, args=(bheap, 7000))


def test_add_bheap_10000(benchmark):
    bheap = BinaryHeap()
    benchmark.pedantic(add_n_elements, args=(bheap, 10000))


def test_add_bheap_20000(benchmark):
    bheap = BinaryHeap()
    benchmark.pedantic(add_n_elements, args=(bheap, 20000))


def test_add_bheap_50000(benchmark):
    bheap = BinaryHeap()
    benchmark.pedantic(add_n_elements, args=(bheap, 50000))


def test_add_bheap_100000(benchmark):
    bheap = BinaryHeap()
    benchmark.pedantic(add_n_elements, args=(bheap, 100000))


def test_pop_bheap_1000(benchmark, bheap):
    benchmark.pedantic(pop_n_elements, args=(bheap, 1000))


def test_pop_bheap_2000(benchmark, bheap):
    benchmark.pedantic(pop_n_elements, args=(bheap, 2000))


def test_pop_bheap_5000(benchmark, bheap):
    benchmark.pedantic(pop_n_elements, args=(bheap, 5000))


def test_pop_bheap_7000(benchmark, bheap):
    benchmark.pedantic(pop_n_elements, args=(bheap, 7000))


def test_pop_bheap_10000(benchmark, bheap):
    benchmark.pedantic(pop_n_elements, args=(bheap, 10000))


def test_pop_bheap_20000(benchmark, bheap):
    benchmark.pedantic(pop_n_elements, args=(bheap, 20000))


def test_pop_bheap_50000(benchmark, bheap):
    benchmark.pedantic(pop_n_elements, args=(bheap, 50000))


def test_pop_bheap_100000(benchmark, bheap):
    benchmark.pedantic(pop_n_elements, args=(bheap, 100000))


#THREEARY HEAP
def test_add_theap_1000(benchmark):
    theap = ThreearyHeap()
    benchmark.pedantic(add_n_elements, args=(theap, 1000))


def test_add_theap_2000(benchmark):
    theap = ThreearyHeap()
    benchmark.pedantic(add_n_elements, args=(theap, 2000))


def test_add_theap_5000(benchmark):
    theap = ThreearyHeap()
    benchmark.pedantic(add_n_elements, args=(theap, 5000))


def test_add_theap_7000(benchmark):
    theap = ThreearyHeap()
    benchmark.pedantic(add_n_elements, args=(theap, 7000))


def test_add_theap_10000(benchmark):
    theap = ThreearyHeap()
    benchmark.pedantic(add_n_elements, args=(theap, 10000))


def test_add_theap_20000(benchmark):
    theap = ThreearyHeap()
    benchmark.pedantic(add_n_elements, args=(theap, 20000))


def test_add_theap_50000(benchmark):
    theap = ThreearyHeap()
    benchmark.pedantic(add_n_elements, args=(theap, 50000))


def test_add_theap_100000(benchmark):
    theap = ThreearyHeap()
    benchmark.pedantic(add_n_elements, args=(theap, 100000))


def test_pop_theap_1000(benchmark, theap):
    benchmark.pedantic(pop_n_elements, args=(theap, 1000))


def test_pop_theap_2000(benchmark, theap):
    benchmark.pedantic(pop_n_elements, args=(theap, 2000))


def test_pop_theap_5000(benchmark, theap):
    benchmark.pedantic(pop_n_elements, args=(theap, 5000))


def test_pop_theap_7000(benchmark, theap):
    benchmark.pedantic(pop_n_elements, args=(theap, 7000))


def test_pop_theap_10000(benchmark, theap):
    benchmark.pedantic(pop_n_elements, args=(theap, 10000))


def test_pop_theap_20000(benchmark, theap):
    benchmark.pedantic(pop_n_elements, args=(theap, 20000))


def test_pop_theap_50000(benchmark, theap):
    benchmark.pedantic(pop_n_elements, args=(theap, 50000))


def test_pop_theap_100000(benchmark, theap):
    benchmark.pedantic(pop_n_elements, args=(theap, 100000))


# FOURARY HEAP
def test_add_fheap_1000(benchmark):
    fheap = FouraryHeap()
    benchmark.pedantic(add_n_elements, args=(fheap, 1000))


def test_add_fheap_2000(benchmark):
    fheap = FouraryHeap()
    benchmark.pedantic(add_n_elements, args=(fheap, 2000))


def test_add_fheap_5000(benchmark):
    fheap = FouraryHeap()
    benchmark.pedantic(add_n_elements, args=(fheap, 5000))


def test_add_fheap_7000(benchmark):
    fheap = FouraryHeap()
    benchmark.pedantic(add_n_elements, args=(fheap, 7000))


def test_add_fheap_10000(benchmark):
    fheap = FouraryHeap()
    benchmark.pedantic(add_n_elements, args=(fheap, 10000))


def test_add_fheap_20000(benchmark):
    fheap = FouraryHeap()
    benchmark.pedantic(add_n_elements, args=(fheap, 20000))


def test_add_fheap_50000(benchmark):
    fheap = FouraryHeap()
    benchmark.pedantic(add_n_elements, args=(fheap, 50000))


def test_add_fheap_100000(benchmark):
    fheap = FouraryHeap()
    benchmark.pedantic(add_n_elements, args=(fheap, 100000))


def test_pop_fheap_1000(benchmark, fheap):
    benchmark.pedantic(pop_n_elements, args=(fheap, 1000))


def test_pop_fheap_2000(benchmark, fheap):
    benchmark.pedantic(pop_n_elements, args=(fheap, 2000))


def test_pop_fheap_5000(benchmark, fheap):
    benchmark.pedantic(pop_n_elements, args=(fheap, 5000))


def test_pop_fheap_7000(benchmark, fheap):
    benchmark.pedantic(pop_n_elements, args=(fheap, 7000))


def test_pop_fheap_10000(benchmark, fheap):
    benchmark.pedantic(pop_n_elements, args=(fheap, 10000))


def test_pop_fheap_20000(benchmark, fheap):
    benchmark.pedantic(pop_n_elements, args=(fheap, 20000))


def test_pop_fheap_50000(benchmark, fheap):
    benchmark.pedantic(pop_n_elements, args=(fheap, 50000))


def test_pop_fheap_100000(benchmark, fheap):
    benchmark.pedantic(pop_n_elements, args=(fheap, 100000))
