# STACKS

# A stack can be thought of as a pile of objects arranged vertically.  The last object added to the stack will be the first one
# removed.  

# In order to remove an element in a stack, all elements which preceed it (are stacked 'on top' of the element we're)
# interested in must be removed first.  As the name implies, you cannot go straight to element in the middle of the stack.

# Uses:  A stack data structure is used whenever the program must access the last element added first.  Common examples include:
#   1. The back button on a web browser

# When to use or avoid:
#   Use:
#       - Whenever last in first out functionality is needed
#       - When data corruption is a concern.  Because there is only one point for data to enter or leave the stack, there is
#         substantially less chance of corruption than with something like a list or array
#   Avoid:
#       - When random access is needed.  Use array instead

# Stack operations:
#   1. Create Stack - Just initialize an empty linked list.  Nothing else to it.
#   2. Push - Insert an element in the stack.  Push always the element to the 'top' of the stack.  
#   3. Pop - Removes al element from the top of the stack
#   4. Peek - Returns the top element of the stack, without deleting/removing that element
#   5. isEmpty - Checks to see whether the stack is empty or not. Used prior to trying peek or pop.
#   6. isFull - In some cases, the stack may have a size limit, this method checks if the stack is full.
#   7. deleteStack - Deletes the stack.

# Stack creation:
# _____________________________________________________________________________________________________________________________________
# Three methods: Python list with no size limit, Python list with size limit, linked list
#   A. Python list with no size limit:
#       -Elements are congiguous in memory
#       -Speed can become a problem as the list grows because Python has to reallocate memory periodically to accomodate growth.

# Creating a stack using Python's built in list functionality is simple:
class ListStackNoLim:
    # Just initialize an empty list for each new stack object we'll create.
    def __init__(self):
        self.list = []
    
    # Modify the str method to enhance printability
    def __str__(self):
        values = self.list.reverse() # First is last and last is first
        values = [str(x) for x in self.list]
        return '\n'.join(values)
    
    # Define the isEmpty method
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    # To push an element into the stack, we can simply use Python's built in list functionality
    def push(self, value):
        self.list.append(value)
        return f"The value: {value} has been sucessfully added to the stack."
    
    # Define the pop method
    def pop(self):
        # First, check to make sure there are actually elements to pop
        if self.isEmpty() == True:
            return "The list is empty, cannot pop."
        else:
            return self.list.pop()
        
    def peek(self):
        # First, check to make sure there are actually elements to peek at
        if self.isEmpty() == True:
            return "The list is empty, cannot peek."
        else:
            return self.list[len(self.list)-1]     
    
    def delete_stack(self):
        self.list = None   



#   B. Python list with no size limit:
class ListStackWithLim:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def isFull(self):
        if len(self.list) == self.maxSize:
            return True
        else:
            return False
    
    def push(self, value):
        if self.isFull() == False:
            self.list.append(value)
            return f"The value: {value} has been sucessfully added to the stack."
        else:
            return "The list is full, the value was not added."
    
    def pop(self):
        if self.isEmpty() == True:
            return "The list is empty, cannot pop."
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty() == True:
            return "The list is empty, cannot peek."
        else:
            return self.list[len(self.list)-1]     
    
    def delete_stack(self):
        self.list = None   
        


#   C. Roll your own linked list:

# First we must define the linked list classes
class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
        # Since we're always working from the front of list, there is no need to define a tail

    # Make the list iterable:
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next

# Next we will define the stack

class LinkedListStack():
    def __init__(self):
        self.list = LinkedList() # A linked list should be inherant to the stack object
    
    def __str__(self):
        values = [str(x.value) for x in self.list]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list.head is None:
            return True
        else:
            return False
    
    def push(self, value):
        new_node = Node(value)
        # If the list is empty, just point head at the newly inserted node
        if self.list.head is None:
            self.list.head = new_node
        # If the list contains nodes already:
        else:
            new_node.next = self.list.head # Point the new node's next property at the current first node, since our new node will be inserted at the beginning of the list
            self.list.head = new_node # Point head at the new node since it is now the first

    def pop(self):
        if self.isEmpty() == True:
            return "There list is empty.  There are no nodes to pop."
        else:
            return_val = self.list.head.value
            self.list.head = self.list.head.next
            return return_val
    
    def peak(self):
        if self.isEmpty() == True:
            return "There list is empty.  There are no nodes to peak at."
        else:
            return self.list.head.value

    def delete_list(self):
        self.list.head = None
        
myStack = LinkedListStack()

myStack.push(1)
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)

print(myStack)
print("")
print("Pop Value:", myStack.pop())
print("")
print(myStack)
print("")
print("Peek Value:", myStack.peak())
print("")
print(myStack)