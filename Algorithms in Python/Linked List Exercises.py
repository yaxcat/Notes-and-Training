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
    def generate_linked_list(self, num_nodes, min_val, max_val):
        # Starting from an empty list so set head and tail to None
        self.head = None
        self.tail = None
        # Generate nodes whose value is a random integer
        for i in range(num_nodes):
            self.add_node(randint(min_val, max_val))
        return self # return the list we have created
    

my_linked_list = LinkedList()
my_linked_list.generate_linked_list(10, 0, 99)
print(my_linked_list)
print(len(my_linked_list))

