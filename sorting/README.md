## Sorting algorithms

Write four sorting functions that implement the following algorithms:
bubble sort, selection sort, merge sort, quick sort.
Each function should take a list as an argument and return a list of
sorted, e.g:
> bubble_sort([3,5,1]) -> [1,3,5]

### Comparison of sorting algorithms
As data for sorting, use the file pan-tadeusz.txt , containing words
separated by white characters. For each of the sorting functions:
check if the function correctly sorts the words loaded from the file,
measure sorting time for lists containing the first n words read from the file
(e.g. n = 1000, 2000, ..., 10000), generate a graph of sorting time vs. list length.