from trees import BinarySearchTree, AVLTree
from random import sample
import sys

sys.setrecursionlimit(50000)
INTEGERS = sample(range(1, 30000), 10000)


def test_create_bst_1000(benchmark):
    benchmark(BinarySearchTree, INTEGERS[:1000])


def test_create_bst_2000(benchmark):
    benchmark(BinarySearchTree, INTEGERS[:2000])


def test_create_bst_5000(benchmark):
    benchmark(BinarySearchTree, INTEGERS[:5000])


def test_create_bst_7000(benchmark):
    benchmark(BinarySearchTree, INTEGERS[:7000])


def test_create_bst_10000(benchmark):
    benchmark(BinarySearchTree, INTEGERS[:10000])


def test_create_avl_1000(benchmark):
    tree = AVLTree()
    benchmark(tree.add, INTEGERS[:1000])


def test_create_avl_2000(benchmark):
    tree = AVLTree()
    benchmark(tree.add, INTEGERS[:2000])


def test_create_avl_5000(benchmark):
    tree = AVLTree()
    benchmark(tree.add, INTEGERS[:5000])


def test_create_avl_7000(benchmark):
    tree = AVLTree()
    benchmark(tree.add, INTEGERS[:7000])


def test_create_avl_10000(benchmark):
    tree = AVLTree()
    benchmark(tree.add, INTEGERS)


def test_find_bst_1000(benchmark):
    tree = BinarySearchTree(INTEGERS)

    def find_n_elements(n):
        for i in range(n):
            tree.find(INTEGERS[i])
    benchmark(find_n_elements, 1000)


def test_find_bst_2000(benchmark):
    tree = BinarySearchTree(INTEGERS)

    def find_n_elements(n):
        for i in range(n):
            tree.find(INTEGERS[i])
    benchmark(find_n_elements, 2000)


def test_find_bst_5000(benchmark):
    tree = BinarySearchTree(INTEGERS)

    def find_n_elements(n):
        for i in range(n):
            tree.find(INTEGERS[i])
    benchmark(find_n_elements, 5000)


def test_find_bst_7000(benchmark):
    tree = BinarySearchTree(INTEGERS)

    def find_n_elements(n):
        for i in range(n):
            tree.find(INTEGERS[i])
    benchmark(find_n_elements, 7000)


def test_find_bst_10000(benchmark):
    tree = BinarySearchTree(INTEGERS)

    def find_n_elements(n):
        for i in range(n):
            tree.find(INTEGERS[i])
    benchmark(find_n_elements, 10000)


def test_find_avl_1000(benchmark):
    tree = AVLTree()
    node = tree.add(INTEGERS)

    def find_n_elements(n):
        for i in range(n):
            tree.find(node, INTEGERS[i])
    benchmark(find_n_elements, 1000)


def test_find_avl_2000(benchmark):
    tree = AVLTree()
    node = tree.add(INTEGERS)

    def find_n_elements(n):
        for i in range(n):
            tree.find(node, INTEGERS[i])
    benchmark(find_n_elements, 2000)


def test_find_avl_5000(benchmark):
    tree = AVLTree()
    node = tree.add(INTEGERS)

    def find_n_elements(n):
        for i in range(n):
            tree.find(node, INTEGERS[i])
    benchmark(find_n_elements, 5000)


def test_find_avl_7000(benchmark):
    tree = AVLTree()
    node = tree.add(INTEGERS)

    def find_n_elements(n):
        for i in range(n):
            tree.find(node, INTEGERS[i])
    benchmark(find_n_elements, 7000)


def test_find_avl_10000(benchmark):
    tree = AVLTree()
    node = tree.add(INTEGERS)

    def find_n_elements(n):
        for i in range(n):
            tree.find(node, INTEGERS[i])
    benchmark(find_n_elements, 10000)


def test_delete_bst_1000(benchmark):
    tree = BinarySearchTree(INTEGERS)
    copy = INTEGERS[:]

    def delete_n_elements(n):
        for i in range(n):
            tree.delete(copy[i])
    benchmark(delete_n_elements, 1000)


def test_delete_bst_2000(benchmark):
    tree = BinarySearchTree(INTEGERS)
    copy = INTEGERS[:]

    def delete_n_elements(n):
        for i in range(n):
            tree.delete(copy[i])
    benchmark(delete_n_elements, 2000)


def test_delete_bst_5000(benchmark):
    tree = BinarySearchTree(INTEGERS)
    copy = INTEGERS[:]

    def delete_n_elements(n):
        for i in range(n):
            tree.delete(copy[i])
    benchmark(delete_n_elements, 5000)


def test_delete_bst_7000(benchmark):
    tree = BinarySearchTree(INTEGERS)
    copy = INTEGERS[:]

    def delete_n_elements(n):
        for i in range(n):
            tree.delete(copy[i])
    benchmark(delete_n_elements, 7000)


def test_delete_bst_10000(benchmark):
    tree = BinarySearchTree(INTEGERS)
    copy = INTEGERS[:]

    def delete_n_elements(n):
        for i in range(n):
            tree.delete(copy[i])
    benchmark(delete_n_elements, 10000)


def test_delete_avl_1000(benchmark):
    tree = AVLTree()
    node = tree.add(INTEGERS)
    copy = INTEGERS[:]

    def delete_n_elements(n):
        for i in range(n):
            tree.delete_node(node, copy[i])
    benchmark(delete_n_elements, 1000)


def test_delete_avl_2000(benchmark):
    tree = AVLTree()
    node = tree.add(INTEGERS)
    copy = INTEGERS[:]

    def delete_n_elements(n):
        for i in range(1, n):
            tree.delete_node(node, copy[i])
    benchmark(delete_n_elements, 2000)


def test_delete_avl_5000(benchmark):
    tree = AVLTree()
    node = tree.add(INTEGERS)
    copy = INTEGERS[:]

    def delete_n_elements(n):
        for i in range(1, n):
            tree.delete_node(node, copy[i])
    benchmark(delete_n_elements, 5000)


def test_delete_avl_7000(benchmark):
    tree = AVLTree()
    node = tree.add(INTEGERS)
    copy = INTEGERS[:]

    def delete_n_elements(n):
        for i in range(1, n):
            tree.delete_node(node, copy[i])
    benchmark(delete_n_elements, 7000)


def test_delete_avl_10000(benchmark):
    tree = AVLTree()
    node = tree.add(INTEGERS)
    copy = INTEGERS[:]

    def delete_n_elements(n):
        for i in range(1, n):
            tree.delete_node(node, copy[i])
    benchmark(delete_n_elements, 10000)
