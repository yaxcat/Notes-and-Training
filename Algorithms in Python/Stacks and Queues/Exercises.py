# EXERCISE 1.
# Use a single list to create three stacks.
# _____________________________________________________________________________________________________________________________

# Why on earth would anyone want to do this???  If you do...

class MultiStack:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.number_stacks = 3
        self.sizes = [None] * self.number_stacks # Keeps track of the number of elements in each stack
        self.list = [None] * (self.stack_size * self.number_stacks) # Stores all three of the stacks

    def isFUll(self, stacknum): 
        if self.sizes[stacknum] == self.stack_size:
            return True
        else:
            return False
    
    def isEmpty(self, stacknum):
        if self.sizes[stacknum] == 0:
            return True
        else:
            return False
    
    # Finds the index of the next open slot in a given stack
    def indexOfTop(self, stacknum):
        # Sincce stacks are LIFO and we want three idividual stacks in one list, first compute the offset number, 
        # which will at least make sure we're accessing the right stack
        offset = stacknum * self.stack_size 
        # Next, compute the index value, which tells us the next open slot in a given stack.  We do this by adding
        # the offset to the number of elements presently in that stack and subtracting one (to avoid going out of range)
        return offset + self.sizes[stacknum] - 1 
    
    def push(self, item, stacknum):
        if self.isFUll(stacknum):
            return "The stack is full"
        else:
            self.sizes[stacknum] += 1 # Increment the size of this stack by one so we can keep track of whats in there
            self.list[self.indexOfTop(stacknum)] = item # Access next open element slot in the stack, set it to item

    def pop(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            value = self.list[self.indexOfTop(stacknum)] # Get the value first, since we're going to need to delete it
            self.list[self.indexOfTop(stacknum)] = None # Next, set the value of the index element we're popping back to None
            self.sizes[stacknum] -= 1 # Finally, decrement the stack's total element count in sizes since we're popping
            return value 
        
    def peek(self, stacknum):
        if self.isEmpty(stacknum):
            return "The stack is empty"
        else:
            return self.list(self.indexOfTop(stacknum))



# EXERCISE 2.
# How would you design a stack which, in additon to push and pop has a function `min` which returns the minimum
# element? Push, pop and min should all operate in O(1) time complexity.
# _____________________________________________________________________________________________________________________________


# Can used a linked list data structure for this problem:
class Node:
    def __init__(self, value=None):
        self.value = value 
        self.next = None

    # Prints the current and next node values
    def __str__(self):
        string = str(self.value)
        if self.next:
            string += ', ' + str(self.next)
            return string


class Stack():
    def __init__(self):
        self.top = None
        self.minNode = None

    # Return the minimum value in the list 
    def min(self):
        if not self.minNode:
            return None # If there is no min node set, just return none
        return self.minNode.value
    
    def push(self, item):
        # If there is a min node and its value is less than whatever item we are pushing in:
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value=self.minNode.value, next=self.minNode)
        # If the item we're pushing has a value less than that of the current min node or the min node is none:
        else:
            self.minNode = Node(value=item, next=self.top)
        self.top = Node(value=item, next=self.top)
        



class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [x.value for x in self]
        return '->'.join(values)