import heapq

# Remove and return the task with the lowest priority value
def extract_min_task(heap):
    # heappop removes the smallest element and restores heap property
    return heapq.heappop(heap)
