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
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    # Prints the current and next node values
    #def __str__(self):
    #    string = str(self.value)
        #if self.next:
        #    string += ', ' + str(self.next)
        #    return string


class Stack():
    def __init__(self):
        self.top = None
        self.minNode = None

    def __iter__(self):
        node = self.top
        while node:
            yield node
            node = node.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return '->'.join(values)


    # Return the minimum value in the list 
    def min(self):
        if not self.minNode:
            return None # If there is no min node set, just return none
        return self.minNode.value
    
    # Push method adds an item to the beginning of the list:
    def push(self, item):
        # If there is a min node and its value is less than whatever item we are pushing in, leave minimum node alone:
        if self.minNode and (self.minNode.value < item):
            self.minNode = Node(value = self.minNode.value, next=self.minNode)
        
        # If the item we're pushing has a value less than that of the current min node or the min node is none:
        else:
            self.minNode = Node(value=item, next=self.minNode) # Set the min node equal to the new value, point this new minimum node value at the next lowest min node (the old min node)
        self.top = Node(value=item, next=self.top) # Add the node to the top of the list
    
    # Pop method removes an item from the beginning of the list:
    def pop(self):
        # If there are no items in the list, just return None.
        if not self.top:
            return None
        self.minNode = self.minNode.next
        item = self.top.value # Get the top's value since we're popping this item and need to return it
        self.top = self.top.next # Delete the node we're popping by changing the next reference
        return item


mystack = Stack()

mystack.push(7)
mystack.push(5)
mystack.push(4)
mystack.push(1)
mystack.push(6)
mystack.push(2)
mystack.push(3)
#mystack.push(-1)

print(mystack, "\n")

print("______________________________________________________________________\n")
print("MIN NODE STACK:")
print("Min Node:", mystack.minNode.value)
print("          ->", mystack.minNode.next.value)
print("             ->", mystack.minNode.next.next.next.value)
print("                 ->", mystack.minNode.next.next.next.next.value)
print("                     ->", mystack.minNode.next.next.next.next.next.value)
print("                         ->", mystack.minNode.next.next.next.next.next.value)
print("                             ->", mystack.minNode.next.next.next.next.next.next.value)
print("______________________________________________________________________\n")

print("Pop A:", mystack.pop())
print("Min Node:", mystack.minNode.value)
print("          ->", mystack.minNode.next.value)
print("Pop B:", mystack.pop())
print("Min Node:", mystack.minNode.value)
print("          ->", mystack.minNode.next.value)
print("Pop C:", mystack.pop())
print("Min Node:", mystack.minNode.value)
print("          ->", mystack.minNode.next.value)
print("Pop D:", mystack.pop())
print("Min Node:", mystack.minNode.value)
print("          ->", mystack.minNode.next.value)
print("Pop E:", mystack.pop())
print("Min Node:", mystack.minNode.value)
print("          ->", mystack.minNode.next.value)
print("\n"*3)



# EXERCISE 3.
# Create a set data structure such that a new stack is created when the stack's maximum capacity limit has been reached.
# _____________________________________________________________________________________________________________________________

class PlateStack():
    def __init__(self, capacity):
        self.capacity = capacity # Stack size limit
        self.stacks = [] # We can use a list of lists for this problem

    def __str__(self):
        return str(self.stacks)
    
    # Pushes an element to the last stack with capacity
    def push(self, item):
        # If there is at least one stack and that stack is not at capacity, just add the item to the last stack:
        if len(self.stacks) > 0 and (len(self.stacks[-1])) < self.capacity:
            self.stacks[-1].append(item)
        # Otherwise, there are either no stacks at all, or there are no stacks with capacity, so:
        else:
            self.stacks.append([item]) # Start a new stack, with its first element being the item we're pushing

    # Pops an element from the last stack with contents
    def pop(self):
        # If the length of the stacks list is greater than zero and the length of the last stack in the stacks list is zero:
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            print("     While triggered:", self.stacks[-1])
            self.stacks.pop() # Pop the empty list itself (empty stack) from the stacks list
        
        # If the length of stacks main is zero, don't return anything
        if len(self.stacks) == 0:
            return None
        # Otherwise jost pop an item from the last stack in stacks
        else:
            return self.stacks[-1].pop()
        
    # Pops an element from a specified stack number:
    def pop_by_stack_num(self, stack_num):
        # If the stack at the number specified has contents:
        if len(self.stacks[stack_num]) > 0:
            return self.stacks[stack_num].pop() # Return the last value in that list
        else:
            return None
        
plates = PlateStack(2)
print("Empty Plates:", plates)
plates.push(1)
#plates.push(2)
#plates.push(3)
#plates.push(4)
#plates.push(5)
#plates.push(6)
print("Empty Plates:", plates)
print("Simple Pop:", plates.pop())
print("Simple Pop:", plates.pop())
#print("Empty Plates:", plates)
#print("Pop by Stack:", plates.pop_by_stack_num(0))
#print("Pop by Stack:", plates.pop_by_stack_num(0))
#print("Empty Plates:", plates)