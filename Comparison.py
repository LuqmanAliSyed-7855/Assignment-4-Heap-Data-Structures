"""Defines and compares three sorting algorithms, Heapsort, Quicksort, and Merge Sort, across 
different input sizes and data distributions such as random, sorted, and reverse-sorted. Each 
algorithm is implemented in a function, and the measure_sort_time() function calculates execution 
time by copying the input list to preserve fairness. Test cases are run for sizes 1000, 5000, 
and 10000 to observe how each algorithm performs on different types of input data. The results 
highlight differences in speed and efficiency, linking them to the theoretical time complexities of the algorithms."""

import random, time

# Heapsort implementation
def heapify(arr, n, i):
    largest = i
    left, right = 2*i + 1, 2*i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# Quicksort using Python’s built-in sort 
def quicksort(arr):
    return sorted(arr)

# Merge Sort implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Measure time for a given sorting function
def measure_sort_time(sort_func, data):
    arr = data.copy()
    start = time.time()
    sort_func(arr)
    return round(time.time() - start, 5)

# Run test
sizes = [1000, 5000, 10000]
distributions = ['random', 'sorted', 'reverse']

for size in sizes:
    print(f"\nInput size: {size}")
    for dist in distributions:
        if dist == 'random':
            data = random.sample(range(size * 2), size)
        elif dist == 'sorted':
            data = list(range(size))
        elif dist == 'reverse':
            data = list(range(size, 0, -1))

        t_heap = measure_sort_time(heapsort, data)
        t_merge = measure_sort_time(merge_sort, data)
        t_quick = measure_sort_time(quicksort, data)

        print(f"{dist.capitalize():<12} | Heap: {t_heap}s | Merge: {t_merge}s | Quick: {t_quick}s")
