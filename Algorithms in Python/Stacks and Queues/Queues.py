# QUEUES

# A queue is much like a stack, but instead of being last-in-first-out, it is first-in-first-out.  Items can only be added to the end
# of the queue, not the beginning or middle.

# Used whenever you need first-in-first-out functionality.  Examples include:
#   - Point of sale system
#   - Printer queue
#
# Queue Operations
#   1. Create queue
#       - Python list without size limit - inefficient, since we must move every element each time we insert a new value 
#       - Python list with size limit - more efficient, becomes a circular queue
#       - Linked list
#   2. Enqueue - Insert a new element
#   3. Dequeue - Remove an element
#   4. Peek
#   5. Is Empty
#   6. Is Full
#   7. Delete Que

# Queue creation:
# _____________________________________________________________________________________________________________________________________
# Much like stacks, there are three methods: Python list with no size limit, Python list with size limit, linked list
#   A. Python list with no size limit:
#       -Elements are congiguous in memory
#       -Speed is a problem since dynamic memory allocation takes time and elements must be shifted forward when a node is removed
#

class Queue:
    def __init__(self):
        self.list = []
    
    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    # May be O(n) or even O(n**2) if the list gets big enough
    def enqueue(self, value):
        self.list.append(value)
        return f"The value: {value} has been added to the queue"
    
    # O(n) time complexity since we have have to shuffle every remaining value forward each time we dequeue an element
    def dequeue(self):
        if self.isEmpty() == True:
            return "The queue is empty, there are no elements to remove"
        return self.list.pop(0) # 0 tells pop() to remove the first element of the list rather than the last (which is the default)

    def peek(self):
        if self.isEmpty() == True:
            return "The queue is empty, there are no elements to peek at"
        return self.list[0]
    
    def delete_queue(self):
        self.list = None

#   B. Python list with a size limit (Circular Queue):
#       - Having a size limit solves both memory allocation and forward shuffle problems that reduce performance
#       - With a circular queue, values in the list are not deleted, just ignored

class CircularQueue:
    def __init__(self, maxSize):
        self.list = [None] * maxSize # Create a list of null values equal to the maxSize argument
        self.max_size = maxSize
        self.start = -1 # Defines the starting position of the list
        self.top = -1 # Defines the ending position of the list

    def __str__(self):
        values = [str(x) for x in self.list]
        return ' '.join(values)
    
    def isFull(self):
        # If adding one more element means we wind up at the starting position, we don't don't have room.  This covers the 'circular'
        # scenario, where we've done some dequeue operations and 'wrapped around' to what was originally the beginning of the list
        if self.top + 1 == self.start:
            return True
        # If adding one more element means we're at the max size, we don't have room.  This covers the non-circular scenario, where
        # we just added a bunch of elements without deleting any. 
        elif self.start == 0 and self.top + 1 == self.max_size:
            return True
        else:
            return False
    
    # In this case, we are only checking if the queue is truly empty.  As the queue is used, values may be dequeued, but they are
    # forgotten and not truly removed.
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False
    
    def enqueue(self, value):
        if self.isFull() == True:
            return "The queue is full"
        else:
            # If the queue is not full, but we've reached the max size of the underlying list, it means we need to put the 'circular'
            # in CircularQueue by wrapping around and starting back at the beginning of the list.  We will overwrite any existing
            # values
            if self.top + 1 == self.max_size:
                self.top = 0
            else:
                self.top += 1 # If we haven't reached the max size of the list, just increment top by one to keep track of where we are
                # We need to account for scenario in which we add the very first element to an empty queue:
                if self.start == -1: # Signifies an empty list
                    self.start = 0
            self.list[self.top] = value # Change the value at the appropriate position
            return f"The value: {value} was inserted at the end of the list in position {self.top}"



myQueue = CircularQueue(5)
print(myQueue)
#print(myQueue.isFull())
print(myQueue.enqueue(1))
print(myQueue.isEmpty()) 
