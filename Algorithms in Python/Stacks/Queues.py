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

myQueue = Queue()
print(myQueue.isEmpty())
myQueue.enqueue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
print(myQueue)
print(myQueue.dequeue())
print(myQueue) 
print(myQueue.peek())