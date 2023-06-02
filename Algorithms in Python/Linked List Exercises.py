# LINKED LIST EXERCISES

from random import randint

# Doubly linked list node class:
class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None
    # For easy printability
    def __str__(self):
        return str(self.value)
    
# List class:
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # Make the list iterable
    def __iter__(self):
        current_node = self.head
        while current_node:
            yield current_node
            current_node = current_node.next
    # For printability
    def __str__(self):
        values = [str(x.value) for x in self] # Since we can iterate over the list, we push printable values into a list iteratively
        return ' -> '.join(values)
    # Define a method to allow us to get the length of the list.  Unlike an array, getting the length should be O(n) time complexity
    def __len__(self):
        result = 0
        node = self.head
        # This is only possible because we defined the __iter__ method above
        while node:
            result += 1
            node = node.next
        return result
    # Adds a node to the end of the list
    def add_node(self, value):
        # If the list is empty:
        if self.head is None:
            new_node = Node(value)
            self.head = new_node
            self.tail = new_node
        # If there are already nodes in the list
        else:
            new_node = Node(value)
            self.tail.next = new_node # Since we're putting the new node at the end of the list, point the current last node's next property at the new node's location
            self.tail = new_node # Point the tail at the new node's location, since its now the last one
        return self.tail
    # Create a linked list using random values
    def generate_linked_list_fr_rand(self, num_nodes, min_val, max_val):
        # Starting from an empty list so set head and tail to None
        self.head = None
        self.tail = None
        # Generate nodes whose value is a random integer
        for i in range(num_nodes):
            self.add_node(randint(min_val, max_val))
        return self # return the list we have created
    # Created this function for testing code in exercise 1
    def generate_linked_list_fr_list(self, input_list):
        for val in input_list:
            self.add_node(val)
        return self

my_linked_list = LinkedList()



# EXERCISE 1
# Write a function to remove duplicates from an unsorted linked list. 
# Input 1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 4 -> 5 
# Output 1 -> 2 -> 3 -> 4 -> 5
#___________________________________________________________________________________________________________________
my_list = [1,3,2,3,4,2,4,3,5,5,5,5,1]
my_linked_list.generate_linked_list_fr_list(my_list)

print(my_linked_list)
print(len(my_linked_list))
print("\n"*3)
 # Overall time complexity is O(n**2) because we have a while loop nested within another while loop.  This is necessary, because 
 # for every node in the list, we must check every other node in the list to eliminate duplicates
def remove_duplicates(linked_list):
    # If there are no nodes in the list, simply return
    if linked_list.head is None:
        return
    # Otherwise, loop through the list. 
    current_node = linked_list.head
    prev_node = None
 
    while current_node: # Loop through all the nodes, this is the node we are checking values against
        runner = current_node
        while runner.next: # Loop through all the nodes in the list starting with the node after the current node, check their values against current node
            if runner.next.value == current_node.value: # If the current node and next node's values are identical
                runner.next = runner.next.next # Set the runner node's next prop to be the node after the one we found a duplicate value for
            else:
                runner = runner.next # Otherwise just carry on
        prev_node = current_node # We'll use this to update the tail at the end
        current_node = current_node.next # Advance forward by one node at a time
 
    linked_list.tail = prev_node  
    return linked_list.head

remove_duplicates(my_linked_list)
print(my_linked_list)
print(len(my_linked_list))
print("\n"*3)


# EXERCISE 2
# Write a find the nth element in a list 
#___________________________________________________________________________________________________________________
my_linked_list = LinkedList()
my_linked_list.generate_linked_list_fr_rand(10, 0, 99)

# If the linked list class has a legnth property, this is relatively straightforward:
print("EXERCISE TWO:")
print("")
print("Linked List:", my_linked_list)
def return_nth_one(linked_list, n):
    if linked_list.head == None:
        return "The list is empty"
    else:
        if n > len(linked_list):
            return "The list length is below the size of the element specified"
        else:
            current_node = linked_list.head
            traversal_distance  = len(linked_list) - n # Defines the nth element from the end of the list
            index = 0
            while index < traversal_distance:
                current_node = current_node.next
                index += 1
            return current_node, current_node.value

print("Return nth One:")
print("     ", return_nth_one(my_linked_list, 4))

# If the linked list class does not have a legnth property, this is a bit more tricky:
def return_nth_two(linked_list, n):
    if linked_list.head == None:
        return "The list list is empty"
    else:
        # In this case, we will use two variables, pointer_a will be the node we return, while pointer_b will be our 'scout'
        # which tells us when pointer_a is at the location we wish to return a value for.
        pointer_a = linked_list.head
        pointer_b = linked_list.head
        index = 0
        # First, advance pointer_b to n places ahead of pointer_a
        while index < n:
            pointer_b = pointer_b.next
            index += 1
        # Next, advance both pointer_a and pointer_b as long as pointer_b is not null.  This will stop us at the correct location
        # to return pointer_a, since we have already advanced pointer_b to n places ahead of pointer_a.  Thus pointer_a will be
        # returned n places before the end of the list.
        while pointer_b:
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next
        
        return pointer_a, pointer_a.value

print("Return nth Two:")
print("     ", return_nth_one(my_linked_list, 4))