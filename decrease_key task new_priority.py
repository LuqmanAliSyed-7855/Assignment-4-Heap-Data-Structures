import heapq

# Update the priority of a task and rebuild the heap
def decrease_key(heap, task_index, new_priority):
    # Update the priority of the task at the given index
    heap[task_index].priority = new_priority

    # Rebuild the heap to maintain the min-heap property
    heapq.heapify(heap)
