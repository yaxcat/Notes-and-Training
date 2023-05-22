# SINGLY LINKED LIST

# A linked list is a sequential collection.  Elements of the collection do not need to have a defined order
# and DO NOT NEED TO BE CONTIGUOUS. Elements of the list can hold any data type and always contain a reference 
#   to the next node in the link. A good analogy is a train. A few properties of a linked list include:
#   1)  Head and tail - each LL contains a beginning and ending node
#   2)  Flexibility - nodes can be added or removed from the list without breaking it
#   3)  Dynamic size - linked list can change size as needed at runtime
#   4)  Sequential access - LLs must be accessed in order from beginning to end which makes them efficient
#       for iteration but less efficient for random access.
#   5)  Limited searchability - since LLs must iterated over until the element is found they are less efficent
#       for search than other data structures like binary trees
# Common use cases of linked lists include:
#   1)  Implementing stacks and Queues
#   2)  Dynamic memory allocation
#   3)  Graphs and trees
#   4)  Playlists
#   5)  File systems


# Linked lists vs. arrays:
# 1) In an array, elements are not separate objects, whereas with a linked list they are.  This means that 
#       

# 1. Creating a singly linked list
#__________________________________________________________________________________
print("1. Creating a singly linked list - ")

# Head/Tail and Node have different properties so we treat them as two separate objects by creating two different
# classes
class Node:
    def __init__ (self, value=None): # Value should be set to null by default
        self.value = value
        self.next = None # Link to the next node should also be set to null by default

class SLinkedList:
    def __init__ (self):
        self.head = None
        self.tail = None
    # Added for printability
    def __iter__(self):
        node = self.head # Start at the head
        while node: # While we have a node...
            yield node # Provides the value and pauses execution of the function
            node = node.next # Move to the next node in the list
    # Added for more printability
    def print_new_node_props(self, node):
            print("     Head:")
            print("         ---Node Address:", self.head)
            print("     Tail:")
            print("         ---Node Address:", self.tail)
            print("     Node:")
            print("         ---Value:", node.value)
            print("         ---Next:", node.next)
    def insert_node(self, value, location):
        new_node = Node(value) # Create a new node, with the value passed in.  It does not have a location yet
        # First, check to see if the linked list is empty.  If it is, this will be the only node:
        if self.head == None: # Default condition when the head is created
            # Since this new node will be the only one in the list, set both head and tail to the new node location
            print("Adding node to empty list:")
            print(" Initial Props:")
            self.print_new_node_props(new_node)
            self.head = new_node
            self.tail = new_node
            print("After node insertion:")
            self.print_new_node_props(new_node)
        # If the list is not empty
        else:
            # If we want to insert the new node at the beginning of the list
            if location == 0:
                new_node.next = self.head # Head stores the location of the current first node, so we pull that ref
                self.head = new_node # We must change head to reference the new first node we just inserted
            # If we want to insert the new node at the end of the list
            elif location == -1:
                print("Adding node to the end of the list:")
                print(" Initial Props:")
                self.print_new_node_props(new_node)
                new_node.next = None # Set the new node's next value to null since we know it will be the final node
                self.tail.next = new_node # Access the last node and set its next property the location of the new node
                self.tail = new_node # We must update the tail's reference to reflect the new node we just created
                print(" After Node Insertion:")
                self.print_new_node_props(new_node)
            # If we want to insert a new node somewhere in the middle of the list
            else:
                print("Adding a node somewhere in the middle of the list")
                current_node = self.head # We must start at the beginning and traverse to find the insertion point
                index = 0
                # Traverse the list until we have reached the location:
                while index < location -1:
                    print(" Traversing the list:")
                    print("     Iteration:")
                    print("         ---", index)
                    print("     Current Node:", current_node)
                    print("         ---Value: ", current_node.value)
                    print("         ---Next:", current_node.next)
                    current_node = current_node.next # current node will take the properties of the next node in the list
                    index += 1
                next_node = current_node.next # Get the node that be after the node we insert
                print(" After traversal:")
                print("     Next Node:")
                print("         ---Next:", next_node)                
                current_node.next = new_node # Since the current node will be before the new node, update its next property
                print("     Current Node:")
                print("         ---Value: ", current_node.value)
                print("         ---Next:", current_node.next)                   
                new_node.next = next_node # Since the next node will be after the new node, update the new node's next property
                print("     New Node:")
                print("         ---Value: ", new_node.value)
                print("         ---Next:", new_node.next)   
                
                # Just in case we're actually inserting at the end
                if current_node == self.tail:
                    self.tail = new_node      
    def delete_node(self, location):
        # First see if the list exists:
        if self.head is None:
            return "The list deoes not exist"
        else:
            # If we need to delete the first node in the list
            if location == 0:
                # If there is only one node in the list
                if self.head == self.tail:
                    # Remove references to the node we are deleting
                    self.head = None
                    self.tail = None
                # If there is more than one node in the list
                else:
                    self.head = self.head.next # Since head stores the first node, self.head.next is accessing the location of node #2, which is what we want
            # If we need to delete the last node in the list
            elif location == -1:
                # If there is only one node in the list
                if self.head == self.tail:
                    # Remove references to the node we are deleting
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node:
                        # Stop at the second to last node
                        if node.next == self.tail:
                            break
                        node = node.next # Carry on iterating through the nodes
                    node.next = None # Once we've broken out of the loop, update the 2nd to last node's next property to none since it is now the last node
                    self.tail = node # We must also update the tail   
            # If we need to delete a node from somewhere in the middle of the list
            else:
                print("Deleting a node somewhere in the middle of the list")
                current_node = self.head # We must start at the beginning and traverse to find the insertion point
                index = 0
                print("Index:", index)
                print("     ---Current Node Location:", current_node.value, current_node)
                # Stops 1 node before the node we want to delete
                print("Entering while loop")
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                    print("     Index:", index)
                    print("             ---Current Node Location:", current_node.value, current_node)
                next_node = current_node.next # Since we stopped 1 before the the node we wish to delete, current_node.next is the node we wish to remove
                current_node.next = next_node.next # Update the current node's next property to be the address of the node AFTER the next node (node we're deleting)
                print("Exited while loop at index", index)
                print("     ---Current Node Location:", current_node.value, current_node)
                print("     ---Next Node Location:", next_node.value, next_node)
                print("         ---Next Node's Next Address:", current_node.next)
    def delete_entire_list(self):
        # Check to make sure the list exists:
        if self.head is None:
            print("There is no list to delete")
        # All we need to do is remove node references in the head and tail, the garbage collector will take care of the rest
        else:
            self.head = None
            self.tail = None        
    def traverse_list(self):
        # First make sure the list exists
        if self.head is None:
            print("The list does not exist")
        # Loop through the list
        else:
            node = self.head
            print("Head")
            print(" ---Next Node:", self.head)
            print("")
            index = 0
            while node is not None:
                print(index, ",", node.value, ",", node)
                print(" ---Next Node:", node.next)
                print("")
                index += 1
                node = node.next # Advance to the next node in the list
    def search_list(self, target_value):
        # First make sure the list exists
        if self.head is None: 
            return "The list does not exist"
        # Loop through the list to see if we can find the value
        else:       
            node = self.head
            while node is not None:
                if node.value == target_value:
                    return (node.value, node)
                node = node.next
            return f"Value: {target_value} not found in list"
# Make some list objects:
my_singly_ll = SLinkedList()
my_singly_ll.insert_node('A', 0)
my_singly_ll.insert_node('B', 1)
my_singly_ll.insert_node('C', 2)
my_singly_ll.insert_node('D', 3)
my_singly_ll.insert_node('E', 4)
my_singly_ll.insert_node('F', 5)


print("")
print("")
print("")
print("TRAVERSING ORIGINAL LIST")
print("------------------------------------------------")
my_singly_ll.traverse_list()
print("")
print(my_singly_ll.search_list('G'))
print("")
print("")
print("INSERTING NODE G")
my_singly_ll.insert_node('G', 3)
print("")
print(my_singly_ll.search_list('G'))
print('')
print("")
print("TRAVERSING NEW LIST")
print("------------------------------------------------")
my_singly_ll.traverse_list()
print("")
print("")
print("")
print("DELETING ITEM FROM LIST")
print("------------------------------------------------")
my_singly_ll.delete_node(3)
print("")
print("")
print("")
print("TRAVERSING NEW LIST")
print("------------------------------------------------")
my_singly_ll.traverse_list()
print("")
print("")
print("")
print("DELETING THE ENTIRE LIST")
print("------------------------------------------------")
print("List object before deletion:", my_singly_ll)
my_singly_ll.delete_entire_list()
print("List object after deletion:", my_singly_ll) # List object still prints, I guess the nodes are cleared?

