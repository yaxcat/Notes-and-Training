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
        return '|'+' '.join(values)+'|'
    
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

    def dequeue(self):
        if self.isEmpty() == True:
            return "The list is empty, there are no items to dequeue."
        else:
            # Save the first item properties to temporary variables
            first_element = self.list[self.start]
            temp_start = self.start
            # If there is only one item in the list:
            if self.start == self.top:
                self.start = -1 # Set start back to -1 since the list is now empty
                self.top = -1 # Set top back to -1 since the list is now empty
            # If we've reached the end of the list, wrap around and start back at the beginning.  Time is a flat circle.
            elif self.start + 1 == self.max_size:
                self.start = 0
            # If there is more than one element in the list and we're somewhere in the middle:
            else:
                self.start += 1 # Just increment the start position by one
            # Finally, tidy up the list and return the leading element
            self.list[temp_start] = None # Set the value of the dequeued element to None so that we can forget about it
            return first_element
    
    def peek(self):
        if self.isEmpty() == True:
            return "The list is empty, there are no items to peek at."
        else:
            return self.list[self.start]
    
    def delete_all_elements(self):
        # Simply null out all elements and set start and top back to -1
        self.list = [None] * self.max_size
        self.start = -1
        self.top = -1
        return "All elements have been deleted from the queue"



#   C. Python list with a Linked List:
#       - No size limit
#       - Very efficient since all operations are TC: O(1) and SC: O(1)
#       - Use a linked list structure whenever possible since its more efficient than using a list or circular list structure

# Linked list stuff:
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return f"{self.value}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next



# Queue stuff
class LinkedListQueue:
    def __init__(self):
        self.ll = LinkedList()

    def isEmpty(self):
        if self.ll.head is None:
            return True
        else:
            return False

    def __str__(self):
        nodes = [str(node) for node in self.ll]
        #first_to_last = reversed(nodes)
        return ' -> '.join(nodes)
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.ll.head is None:
            self.ll.head = new_node
            self.ll.tail = new_node
        # Since this is a queue, new nodes will be added at the end
        else:
            self.ll.tail.next = new_node
            self.ll.tail = new_node

    def dequeue(self):
        if self.isEmpty() == True:
            return "The list is empty, there are no elements to dequeue."
        else:
            # If there is only one node in the list
            if self.ll.head == self.ll.tail:
                removed_node = self.ll.head
                self.ll.head = None
                self.ll.tail = None
                return removed_node
            # If there is more than one node in the list
            else:
                removed_node = self.ll.head
                self.ll.head = self.ll.head.next
                return removed_node
    def peek(self):
        if self.isEmpty() == True:
            return "The list is empty, there are no nodes to peek at."
        else:
            return self.ll.head
    
    def delete_entire_queue(self):
        self.ll.head = None
        self.ll.tail = None
            

myLLQ = LinkedListQueue()
myLLQ.enqueue('A')
myLLQ.enqueue('B')
myLLQ.enqueue('C')

print(myLLQ)

print(myLLQ.dequeue())
print("List:", myLLQ)
print(myLLQ.dequeue())
print("List:", myLLQ)
print(myLLQ.dequeue())
print("List:", myLLQ)
print(myLLQ.dequeue())
print("List:", myLLQ)