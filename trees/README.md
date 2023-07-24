## Trees

Prepare implementations of the following trees:
- Binary Search Tree (BST tree),
- AVL tree.

Required operations:
- inserting an element in the tree,
- searching for an element in the tree,
- deleting an element from the tree,
- displaying the tree on the screen (in an arbitrary but readable way).

### Tree comparison
Generate an input list of numbers (e.g. 10000 random numbers from 1 to
30000), which will be used further to test performance.

For each of the trees:
- measure the tree creation time based on the first n numbers of the input list
(e.g. n = 1000, 2000, ..., 10000),
- measure the search times of the first n numbers of the input list (e.g. n = 1000,
2000, ..., 10000) in a tree that for each n was created on the
based on the entire input list,
- measure the times for removing the first n numbers of the input list (e.g. n = 1000, 2000,..., 10000) in a tree that for each n was created based on the entire
input list.

For each operation, generate summary graphs (one graph for both types of
trees) showing the dependence of the execution time of the operation on the number of elements.