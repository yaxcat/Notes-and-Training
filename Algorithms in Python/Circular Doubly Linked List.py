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
                pass

print("CREATING A NEW CDLL")
print("------------------------------------------------")
my_cdll = CircularDoublyLinkedList()
print(my_cdll.createCDLL("C"))
print("\n"*3)
print("TRAVERSING ENTIRE LIST FORWARD")
print("------------------------------------------------")
my_cdll.traverse_and_print('forward')
print("\n"*3)
print("INSERTING A NEW NODE AT THE BEGINNING OF THE LIST")
print("------------------------------------------------")
print(my_cdll.insert_node('B', 0))
print(my_cdll.insert_node('A', 0))
print(my_cdll.insert_node('!!!', -1))
print("\n"*3)
print("TRAVERSING ENTIRE LIST FORWARD")
print("------------------------------------------------")
my_cdll.traverse_and_print('forward')
print("\n"*3)
