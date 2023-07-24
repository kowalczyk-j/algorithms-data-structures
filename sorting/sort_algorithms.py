def selection_sort(a):
    for i in range(len(a)):
        min = i
        for j in range(i+1, len(a)):
            if a[j] < a[min]:
                min = j
        t = a[i]
        a[i] = a[min]
        a[min] = t
    return a


def quicksort(a, low, high):
    if low >= high:
        return

    partition_item = a[low]
    i = low + 1
    j = high

    while True:
        while i <= j and a[j] >= partition_item:
            j -= 1
        while i <= j and a[i] <= partition_item:
            i += 1
        if i <= j:
            a[i], a[j] = a[j], a[i]
        else:
            break
    a[low], a[j] = a[j], a[low]

    quicksort(a, low, j-1)
    quicksort(a, j+1, high)


def bubble_sort(list):
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if list[j] > list[j+1]:
                temp = list[j+1]
                list[j+1] = list[j]
                list[j] = temp
    return list


def merge(left_list, right_list):
    merged_list = []
    left_i = 0
    right_i = 0
    while left_i < len(left_list) and right_i < len(right_list):
        if left_list[left_i] < right_list[right_i]:
            merged_list.append(left_list[left_i])
            left_i += 1
        else:
            merged_list.append(right_list[right_i])
            right_i += 1
    merged_list += left_list[left_i:]
    merged_list += right_list[right_i:]
    return merged_list


def merge_sort(list):
    if len(list) <= 1:
        return list
    middle = len(list)//2
    left_list = merge_sort(list[:middle])
    right_list = merge_sort(list[middle:])
    return merge(left_list, right_list)
