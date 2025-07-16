"""Defines a Task class with attributes such as task ID, priority, arrival time, and deadline, 
along with a comparison method to support priority-based ordering. A list is used as the underlying 
structure for the heap, and the heapq module manages insertion and extraction of tasks based 
on priority. Tasks are added to the queue using heappush and are removed in order using heappop, 
ensuring the task with the smallest priority value is processed first. The output displays tasks 
being processed in the correct priority order according to a min-heap configuration.
"""

import heapq

# Define a Task class to store task information
class Task:
    def __init__(self, task_id, priority, arrival_time, deadline):
        # Unique identifier for the task
        self.task_id = task_id
        
        # Numerical value representing task priority
        self.priority = priority
        
        # Time at which the task arrives in the system
        self.arrival_time = arrival_time
        
        # Deadline by which the task should be completed
        self.deadline = deadline

    # Less-than method used by heapq to compare tasks based on priority
    def __lt__(self, other):
        return self.priority < other.priority

    # String representation of a task for easy output
    def __repr__(self):
        return f"Task ID {self.task_id}, Priority {self.priority}, Arrival {self.arrival_time}, Deadline {self.deadline}"

# Create an empty list to serve as the heap
task_queue = []

# Add tasks to the priority queue using heapq
heapq.heappush(task_queue, Task("T1", 2, 0, 10))  # Task with priority 2
heapq.heappush(task_queue, Task("T2", 1, 1, 5))   # Task with priority 1
heapq.heappush(task_queue, Task("T3", 3, 2, 15))  # Task with priority 3

# Process tasks in order of priority using heappop
while task_queue:
    current_task = heapq.heappop(task_queue)
    print("Processing", current_task)
