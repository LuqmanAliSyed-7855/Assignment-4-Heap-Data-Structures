"""The Heapsort begins by building a max-heap from the unsorted array using the heapify() 
function, which ensures that each subtree maintains the max-heap property by comparing a node
 with its children and swapping if necessary. Once the max-heap is constructed, the algorithm
repeatedly extracts the maximum element (the root), places it at the end of the array, and 
reduces the heap size. After each extraction, `heapify()` is called again to maintain the heap structure. 
This process continues until all elements are sorted in ascending order, resulting in an efficient 
in-place sorting algorithm with O(n log n) time complexity.
"""


def heapify(arr, n, i):
    
    # Ensure the subtree rooted at index 'i' satisfies the max-heap property.
    largest = i           # Assume the root is the largest
    left = 2 * i + 1      # Left child index
    right = 2 * i + 2     # Right child index

    # If left child exists and is greater than the current largest
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest is not the root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

def heapsort(arr):
    """
    Performing the Heapsort algorithm to sort the array in ascending order.
    Build a max-heap from the array.
    Repeatedly extract the maximum element and heapify the remaining elements.
    """
    n = len(arr)

    # Build a max-heap 
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Swap the root with the last element
        arr[0], arr[i] = arr[i], arr[0]

        # Heapify the reduced heap
        heapify(arr, i, 0)

# Example usage
if __name__ == "__main__":
    array = [20, 1, 15, 8, 3, 10, 5]
    print("Original array:", array)
    heapsort(array)
    print("Sorted array:", array)
