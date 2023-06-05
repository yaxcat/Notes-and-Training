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


# EXERCISE 3
# Partition a linked list around some value, x, such that all values less than x are positioned to its right and all values greater
# than x are to its left.  The order of the values to the right and left of x does not matter as long they are less than or greater
# x respectively.
#___________________________________________________________________________________________________________________
my_linked_list = LinkedList()
my_linked_list.generate_linked_list_fr_rand(10, 0, 99)

# If the linked list class has a legnth property, this is relatively straightforward:
print("\n"*3)
print("EXERCISE THREE:")
print("")
print("Linked List:", my_linked_list)

def partition_list(linked_list, x):
    current_node = linked_list.head
    linked_list.tail = linked_list.head
    # Loop through all the nodes
    while current_node:
        next_node = current_node.next
        current_node.next = None # Set the current node's next property to none because the initial value will be overwritten anyway
        # If the node's value is less than x, partition by inserting it at the beginning of the list
        if current_node.value < x:
            current_node.next = linked_list.head # Since the node is going at position 0, its next prop should be equal to whatever is currently in the head, since that node will now be second
            linked_list.head = current_node # Update the head to point to the new node that is now first in line
        # If the node's value is greater than x, partition by inserting it at the end of the list
        else:
            linked_list.tail.next = current_node # Since we're inserting at the end of the list, point the current last node's next prop at the node we will be inserting at the end
            linked_list.tail = current_node # Point the tail at the new node we've inserted at the end
        current_node = next_node
    # If whatever our final node winds up being has a next prop, set that to null since we don't want to turn this into a circular list
    if linked_list.tail.next is not None:
        linked_list.tail.next = None

print("Partitioned list:")
partition_list(my_linked_list, 50)
print("     ", my_linked_list)

# EXERCISE 4
# You have two numbers represented by linked lists where each node contains a single digit. The digits are stored in reverse order
# such that the ones digit is at the head of the list.  Write a function that adds the two numbers and returns the sum as a linked
# list.
#___________________________________________________________________________________________________________________
ll1 = LinkedList()
ll2 = LinkedList()
ll1.generate_linked_list_fr_rand(3, 0, 9)
ll2.generate_linked_list_fr_rand(3, 0, 9)
print("\n"*3)
print("EXERCISE FOUR:")
print("")
print("List 1:", ll1)
print("List 2:", ll2)

def return_vals_reversed(linked_list):
    current_node = linked_list.head
    values = []
    while current_node:
        values.append(str(current_node.value))
        current_node = current_node.next
    values = list(reversed(values))
    reversed_sequence = ''
    reversed_sequence = reversed_sequence.join(values)
    return int(reversed_sequence)

def add_lists(ll_1, ll_2):
    ll1_vals = return_vals_reversed(ll_1)
    ll2_vals = return_vals_reversed(ll_2)
    print("List 1 Digits:", ll1_vals)
    print("List 2 Digits:", ll2_vals)
    total = list(reversed(str(ll1_vals + ll2_vals)))
    print("     Total:", total)
    new_linked_list = LinkedList()
    for digit in total:
        new_linked_list.add_node(digit)
    return new_linked_list


new_linked_list = add_lists(ll1, ll2)
print(new_linked_list)


# EXERCISE 5
# Given two singly linked lists, determine if the two lists intersect. Return the intersecting node. Note that the intersection
# is based on the reference, not the value.  That is, if the kth node of the first list is the exact same node by reference
# as the second linked list, then they are intersecting.
#___________________________________________________________________________________________________________________
# TC: O(a + b) because the length of the lists can be different and impossible to anticipate
def find_intersection(ll1, ll2):
    # Determine whether or not the lists intersect at all
    if ll1.tail != ll2.tail: # If the lists intersect, their tails will be the same
        return "The two lists do not intersect"
    else:
        len1 = len(ll1)
        len2 = len(ll2)
        # Identify the longer and shorter lists
        shorter = ll1 if len1 < len2 else len2
        longer = ll1 if len1 > len2 else len2
        # Calculate the difference between them, this will be used to sync up our iteration over the lists
        difference = len(longer) - len(shorter)

        longer_node = longer.head
        shorter_node = shorter.head

        # Since we know that the tails of two intersecting lists will be the same, we also know that nodes at the begininning of
        # the longer list will be 'before' the starting node of the shorter list, and it is therefore impossible to have an
        # intersection there.  Because of this, we must advance node of the longer list to be equal to the starting node of the 
        # shorter list before doing the comparison.
        for i in range(difference):
            longer_node = longer_node.next

        # Loop through each list and compare nodes:
        while longer_node is not shorter_node:
            longer_node = longer_node.next
            shorter_node = shorter_node.next
        return longer_node
