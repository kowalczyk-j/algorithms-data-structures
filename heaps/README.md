## Heaps

Implement three complete heaps: 2-ary, 3-ary and 4-ary. Each of the heaps
implement in an array (a list in Python).

Required operations:
- inserting an element into a heaps,
- deleting the top of a heap,
- displaying the heaps on the screen (in an arbitrary but readable way).

### Comparison of heaps
Generate an input list of numbers (e.g. 100000 random numbers ranging from 1 to
300000), which will be used further to test performance.

For each of the heaps:
- measure the heap creation time based on the first n numbers of the input list
(e.g. n = 10000, 20000, ..., 100000),
- measure the time to perform n operations to remove the top of the heaps (e.g. n = 10000, 20000, ..., 100000) in a heap that, for each n, was created on the
based on the entire input list.

For each operation, generate summary graphs (one graph for the three types of
heaps) showing the dependence of the execution time of the operation on the number of elements/executions.