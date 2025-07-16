import heapq

# Insert a new task into the min-heap
def insert_task(heap, task):
    # heappush maintains the min-heap property after insertion
    heapq.heappush(heap, task)
