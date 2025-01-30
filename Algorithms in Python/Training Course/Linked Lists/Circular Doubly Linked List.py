# CIRCULAR DOUBLY LINKED LIST

# Set up classes to build the lists
class Node:
    # Initialize the node
    def __init__(self, value):
        # Set the value to whatever we pass in and prev & next props to null by default
        self.value = value
        self.prev = None
        self.next = None

class CircularDoublyLinkedList():
    # Initialize the list
    def __init__(self):
        self.head = None
        self.tail = None
    # Create a new list object, which will have a single node
    def createCDLL(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        # Since this is a CDLL and we know we only have the one node, set both the prev & next props equal to the new node
        new_node.prev = new_node
        new_node.next = new_node
        return "Circular Doubly Linked List created successfully."
    # Print out some properties that characterize a given node
    def print_node_props(self, current_node, index):
        print(" Index:", index)
        print("     Current Node:", current_node.value, " | ", current_node)
        print("         Prev:", current_node.prev.value, " | ", current_node.prev)
        print("         Next:", current_node.next.value, " | ", current_node.next)
    # Traverse the list and print some of its properties
    def traverse_and_print(self, direction):
        if direction == 'forward':
            if self.head is None:
                print("The list is empty")
            else:
                current_node = self.head
                index = 0
                print("Head:", self.head.value, " | ", self.head)
                while current_node != self.tail:
                    self.print_node_props(current_node, index)
                    current_node = current_node.next
                    index += 1
                self.print_node_props(current_node, index)
                print("Tail:", self.tail.value, " | ", self.tail)
        elif direction == 'backward':
            if self.head is None:
                print("The list is empty")
            else:
                current_node = self.tail
                index = 0
                print("Tail:", self.tail.value, " | ", self.tail)
                while current_node != self.tail:
                    self.print_node_props(current_node, index)
                    current_node = current_node.prev
                    index += 1
                self.print_node_props(current_node, index)
                print("Head:", self.head.value, " | ", self.head)
        else:
            print("The direction is invalid.  Please use either 'forward' or 'backward'.")
    # Insert a node at a given position in the list
    def insert_node(self, value, position):
        # If the head is null, it means there are no nodes in the list and this will be both our first and last node
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = new_node
            new_node.next = new_node
            return "Inserted a new node in an empty list."
        # There is at least one existing node in the list
        else:
            # Insert at the beginning of the list
            if position == 0:
                new_node.prev = self.head.prev # Since we're inserting this node at the start of the CDLL, we must set its prev property to the last node in the list
                new_node.next = self.head # Since we're displacing the current first node (making it second in the list), we must set the next prop of the new (first) node to the address of the current first node we are displacing
                self.head.prev = new_node # Since we have a new first node, we must change the current first node's prev reference to point to the new node we are inserting
                self.tail.next = new_node # Point the last node in the list's next prop to the new node we are inserting since this is a CDLL
                self.head = new_node # Point the head at the newly inserted first node
                return "New node inserting at the beginning of the list."
            # Insert at the end of the list
            elif position == -1:
                new_node.prev = self.tail # Set the new last node's prev reference to point to the current last node, since we are taking its place
                new_node.next = self.tail.next # Set the new last node's next reference to the first node in the list since this is a CDLL
                self.tail.next = new_node # Update the next prop of the current last node to point to the new node, since the current node will now be second to last place
                self.head.prev = new_node # Update the first node's prev prop to point to the new node since this is a CDLL.
                self.tail = new_node # Finally, point the tail at the new last node.
            # Insert somewhere in the middle of the list
            else:
                current_node = self.head
                index = 0
                while index < position -1:
                    current_node = current_node.next
                    index += 1
                next_node = current_node.next # Node that will be after the one we delete
                current_node.next = new_node # Set the next prop of the current node to point to the node we're inserting
                next_node.prev = new_node # Set the prev prop of the node after the one we're inserting to point to the new node
                new_node.prev = current_node # Set the prev property of the new node to that of the current node, since we are inserting in front of it
                new_node.next = next_node # Set the next property of the new node to point to the next node, since our new node will be inserted directly behind it
                return f"Node inserted in the middle of the list at postion {position}"
    # Search for a given node value and return it if found
    def search_for_node_val(self, value):
        # Check to make sure the list has nodes to search
        if self.head is None:
            return "There are no nodes to search for."
        else:
            current_node = self.head
            while current_node:
                if current_node.value == value:
                    return current_node
                # Since this is a circular list, we need a second if statement to break out of the loop if we get to the end without finding anything
                if current_node == self.tail:
                    return f"The node with value: {value} could not be found."
                current_node = current_node.next
    # Delete a node at a given position
    def delete_node_by_position(self, position):
        # First check to see if there are nodes to delete
        if self.head is None:
            return "There are no nodes to delete."
        else:
            # Delete the starting node of the list
            if position == 0:
                # If there is only one node in the list:
                if self.head == self.tail:
                    #First, remove self-references from the node
                    self.head.prev = None
                    self.head.next = None
                    # Next, remove references to that node in head and tail
                    self.head = None
                    self.tail = None
                else:
                    node_to_delete = self.head # Node we wish to delete
                    self.tail.next = node_to_delete.next # Set the next property of the last node in the list to point to the node after the node we wish to delete
                    self.head = node_to_delete.next # Point the head to the node after the node we wish to delete since it will become the first node in the list
                    self.head.prev = self.tail # Since second node in the list is becoming the first node, we must update its prev property to point to the last node in the list
            # Delete the final node in the list
            elif position == -1:
                # If there is only one node in the list:
                if self.head == self.tail:
                    #First, remove self-references from the node
                    self.head.prev = None
                    self.head.next = None
                    # Next, remove references to that node in head and tail
                    self.head = None
                    self.tail = None
                else:
                    node_to_delete = self.tail # Node we wish to delete
                    self.head.prev = node_to_delete.prev # Set the prev property of the first node in the list to point to the second to last node in the list (since we're deleting the last one)
                    self.tail = node_to_delete.prev # Set the tail to point to the second to last node in the list
                    self.tail.next = self.head # Since the second to last node in the list is now the last, we must update its next prop to point to the first node in the list
            # Delete a node from the middle of the list
            else:
                current_node = self.head
                index = 0
                while index < position - 1:
                    current_node = current_node.next
                    index += 1
                node_to_delete = current_node.next # Since we exit the loop at the node before the one we wish to delete, the deletable node = current_node.next
                current_node.next = node_to_delete.next 
                node_to_delete.next.prev = current_node
    
    def delete_entire_list(self):
        if self.head is None:
            return "There is no list to delete"
        else:
            self.tail.next = None # Sever the forward link between the last node in the list the first
            current_node = self.head
            # Loop through the list a sever the backward link between adjacent nodes.  No need for a break. YOLO.
            while current_node:
                current_node.prev = None
                current_node = current_node.next
            # Finally, sever head and tail links
            self.head = None
            self.tail = None
            return "The CDLL has been deleted."

print("CREATING A NEW CDLL")
print("------------------------------------------------")
my_cdll = CircularDoublyLinkedList()
print(my_cdll.createCDLL("A"))
print("\n"*3)
print("TRAVERSING ENTIRE LIST FORWARD")
print("------------------------------------------------")
my_cdll.traverse_and_print('forward')
print("\n"*3)
print("INSERTING A NEW NODE AT THE BEGINNING OF THE LIST")
print("------------------------------------------------")
print(my_cdll.insert_node('F', -1))
print(my_cdll.insert_node('B', 1))
print(my_cdll.insert_node('C', 2))
print(my_cdll.insert_node('D', 3))
print(my_cdll.insert_node('E', 4))
print("\n"*3)
print("INSERTING A NEW NODE AT POSITION 3")
print("------------------------------------------------")
print(my_cdll.insert_node("!!!", 3))
print("\n"*3)
print("TRAVERSING ENTIRE LIST FORWARD")
print("------------------------------------------------")
my_cdll.traverse_and_print('forward')
print("\n"*3)
print("SEARCHING FOR NODE")
print("------------------------------------------------")
print(my_cdll.search_for_node_val('F'))
print("\n"*3)
print("DELETING NODE")
print("------------------------------------------------")
my_cdll.delete_node_by_position(3)
print("\n"*3)
print("TRAVERSING ENTIRE LIST FORWARD")
print("------------------------------------------------")
my_cdll.traverse_and_print('forward')
print("\n"*3)
print("DELETING ENTIRE LIST")
print("------------------------------------------------")
print(my_cdll.delete_entire_list())
print("\n"*3)
print("TRAVERSING ENTIRE LIST FORWARD")
print("------------------------------------------------")
my_cdll.traverse_and_print('forward')
print("\n"*3)