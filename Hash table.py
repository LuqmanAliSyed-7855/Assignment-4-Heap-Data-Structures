"""Defines a hash table using chaining, where each index contains a list to handle collisions by 
storing multiple key-value pairs. It includes functions for inserting, searching, and deleting 
keys using a hash function based on Python’s built-in hash() combined with modulo. The table 
structure ensures efficient performance, and the display function provides a view of the 
current bucket contents.
"""

class HashTable:
    def __init__(self, size=10):
        # Initialize the hash table with a fixed number of buckets 
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash_function(self, key):
        # Simple universal-style hash function using built-in hash and modulo
        return hash(key) % self.size

    def insert(self, key, value):
        # Insert a key-value pair into the hash table
        index = self._hash_function(key)
        bucket = self.table[index]
        
        # Update value if key already exists
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        # Otherwise, append new key-value pair
        bucket.append((key, value))

    def search(self, key):
        # Search for a value associated with the given key
        index = self._hash_function(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return None  # Return None if key not found

    def delete(self, key):
        # Delete a key-value pair from the hash table
        index = self._hash_function(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False  # Return False if key not found

    def display(self):
        # Display the entire hash table
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")

# Example Usage
ht = HashTable(size=7)  # Create a hash table of size 7
ht.insert("apple", 10)
ht.insert("banana", 20)
ht.insert("grape", 30)
ht.insert("orange", 40)

print("Search 'banana':", ht.search("banana"))  

ht.delete("banana")
print("Search 'banana' after deletion:", ht.search("banana"))  

ht.display()
