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
plates.push(2)
plates.push(3)
plates.push(4)
plates.push(5)
plates.push(6)
print("Empty Plates:", plates)
print("Simple Pop:", plates.pop())
print("Simple Pop:", plates.pop())
print("Empty Plates:", plates)
print("Pop by Stack:", plates.pop_by_stack_num(0))
print("Pop by Stack:", plates.pop_by_stack_num(0))
print("Empty Plates:", plates)
print("\n"*3)

# EXERCISE 4.
# Create a queue class which implements a queue using two stacks.
# _____________________________________________________________________________________________________________________________
class Stack2():

    def __init__(self):
        self.list = []
    
    def __len__(self):
        return len(self.list)
    
    # Append an item to the end of the list
    def push(self, item):
        self.list.append(item)

    # Pop an item from the end of the list
    def pop(self):
        if len(self.list) == 0:
            return None
        return self.list.pop()
    

class QueueViaStack():
    # Each Queue object should have two stacks to shuffle items between
    def __init__(self):
        self.inStack = Stack2()
        self.outStack = Stack2()

    # Add items to the queue
    def enqueue(self, item):
        self.inStack.push(item)

    # Remove elements from the 'in stack' and put them in the 'out stack'
    def dequeue(self):
        # First, the order of outStack elements must be reversed.  So if inStack = [1,2,3,4], outStack = [4,3,2,1]
        while len(self.inStack): # While len(inStack) > 0
            self.outStack.push(self.inStack.pop()) # Remove the value from in stack and append it to out stack
        # Next, pop the outStack result - This gives us the FIFO behavior we would expect of a queue, since first is now last (i.e. our popped value would be 1)
        result = self.outStack.pop()
        # Finally, put everything back to the way it was, so we run this process as many times as we like
        while (len(self.outStack)):
            self.inStack.push(self.outStack.pop()) # inStack is now empty, so we just pop outStack until it is empty, which reverses the order of elements back to what it was originally (minus the value we popped)
        
        return result
    

my_queue = QueueViaStack()

my_queue.enqueue(1)
my_queue.enqueue(2)
my_queue.enqueue(3)
my_queue.enqueue(4)
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print(my_queue.dequeue())
print("\n"*3)


# EXERCISE 5.
# An animal shelter which holds only dogs and cats operates on a first-in, first-out basis.  People must adopt either
# the oldest (based on arrival time) of all animals at the shelter, or they can select whether they would prefer a dog
# or a cat, and recieve the oldest animal of that type.  Create a data structure to maintain this system and create
# methods for enqueueAny, dequeueAny, dequeueDog, dequeueCat
# _____________________________________________________________________________________________________________________________

# Simpler than it sounds, since there is no requirement that we keep all the animals in a single list
class AnimalShelter():
    # Initialize two lists, one to hold dogs, and the other cats
    def __init__(self):
        self.cats = []
        self.dogs = []

    def enqueue(self, animal, animal_type):
        if animal_type == 'Cat':
            self.cats.append(animal)
        elif animal_type == 'Dog':
            self.dogs.append(animal)
        else:
            return "That type of animal is not allowed at the shelter"
    
    def dequeuCat(self):
        if len(self.cats) == 0:
            return None
        else:
            return self.cats.pop(0) # Zero causes pop to return the first element in the list, rather than the last (which is the default)
    
    def dequeueDog(self):
        if len(self.dogs) == 0:
            return None
        else:
            return self.dogs.pop(0)
        
    def dequeueAny(self):
        if len(self.cats) == 0:
            result = self.dogs.pop(0)
        else:
            result = self.cats.pop(0)
        return result