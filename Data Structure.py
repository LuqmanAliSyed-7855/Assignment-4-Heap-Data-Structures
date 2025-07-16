"""Defines a Task class with attributes such as task ID, priority, arrival time, and deadline, 
along with a comparison method to support priority-based ordering. A list is used as the underlying 
structure for the heap, and the heapq module manages insertion and extraction of tasks based 
on priority. Tasks are added to the queue using heappush and are removed in order using heappop, 
ensuring the task with the smallest priority value is processed first. The output displays tasks 
being processed in the correct priority order according to a min-heap configuration.
"""

import heapq
import itertools

# Task class to hold task details
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        self.task_id = task_id
        self.priority = priority  # Lower values mean higher priority in a min-heap
        self.arrival_time = arrival_time
        self.deadline = deadline

    def __lt__(self, other):
        return self.priority < other.priority  # Required for comparison in heapq

    def __repr__(self):
        return f"(ID: {self.task_id}, P: {self.priority}, A: {self.arrival_time}, D: {self.deadline})"


# Min-Heap based Priority Queue
class TaskScheduler:
    def __init__(self):
        self.heap = []
        self.entry_finder = {}  # Map from task_id to [priority, count, task]
        self.REMOVED = "<REMOVED>"
        self.counter = itertools.count()  # Unique sequence count to avoid tie

    def insert(self, task):
        """Insert a task into the priority queue. O(log n)"""
        if task.task_id in self.entry_finder:
            self.remove_task(task.task_id)
        count = next(self.counter)
        entry = [task.priority, count, task]
        self.entry_finder[task.task_id] = entry
        heapq.heappush(self.heap, entry)

    def remove_task(self, task_id):
        """Mark an existing task as removed. O(1)"""
        entry = self.entry_finder.pop(task_id)
        entry[-1] = self.REMOVED

    def extract_min(self):
        """Remove and return the task with the lowest priority (highest importance). O(log n)"""
        while self.heap:
            priority, count, task = heapq.heappop(self.heap)
            if task != self.REMOVED:
                del self.entry_finder[task.task_id]
                return task
        raise KeyError("Priority queue is empty")

    def decrease_key(self, task_id, new_priority):
        """Decrease the priority of a task and reheapify. O(log n)"""
        if task_id not in self.entry_finder:
            raise KeyError("Task not found")
        old_task = self.entry_finder[task_id][-1]
        self.remove_task(task_id)
        updated_task = Task(old_task.task_id, new_priority, old_task.arrival_time, old_task.deadline)
        self.insert(updated_task)

    def is_empty(self):
        """Check if the priority queue is empty. O(1)"""
        return not any(task != self.REMOVED for _, _, task in self.heap)

# Sample usage
if __name__ == "__main__":
    scheduler = TaskScheduler()
    
    scheduler.insert(Task("T1", 5, "10:00", "10:30"))
    scheduler.insert(Task("T2", 3, "10:01", "10:20"))
    scheduler.insert(Task("T3", 4, "10:02", "10:25"))

    print("Extracted:", scheduler.extract_min())  # T2 should be returned

    scheduler.decrease_key("T1", 2)  # Increase priority of T1

    while not scheduler.is_empty():
        print("Next task:", scheduler.extract_min())
