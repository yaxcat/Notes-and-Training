# DOUBLY LINKED LISTS

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.list_len = 0
    # Create the DLL
    def createDLL(self, value):
        node = Node(value)
        # All we need to do is set the head/tail refs.  
        # No need to mess with node.next and node.prev since this list isn't circular
        self.head = node
        self.tail = node
        return "DLL created"
    # Insert a node in the DLL
    def insert_node(self, value, location):
        # If the list is empty, return an error message.  Doesn't have to end in an error, but for the puroses of this training, we'll leave it as is
        if self.head == None:
            return "The list is empty, cannot insert node"
        # If the list is not empty:
        else:
            new_node = Node(value) # Instantiate the new node object
            # If we want to insert a node at the beginning of the list
            if location == 0:
                new_node.next = self.head # Set the new node's next property to that of the current first node
                self.head.prev = new_node # Set the prev property of the original first node to that of the new node we're inserting, since it is becoming the first node now
                self.head = new_node # Update the head reference to point to the new node we're inserting
                return("Node with value {value} inserted at the beginning of the list")
            # If we want to insert a node at the end of the list
            elif location == -1:
                new_node.prev = self.tail # Since the node we're inserting takes the place of the current 'last node', set our new last node's prev property to point to the current last node
                self.tail.next = new_node # Set the next property of the current last node to point to the new node we are inserting
                self.tail = new_node # Point the tail to our new last node
                return("Node with value {value} inserted at the end of the list")
            # If we want to insert a node somewhere in the middle of the list
            else:
                # Loop until two nodes before the place we wish to insert the new node:
                current_node = self.head
                index = 0
                while index < location - 1:
                    current_node = current_node.next
                    index += 1
                # Upon loop exit, the current node will be the node before the position we are inserting into
                # This is all confusing as shit.  See the excel sheet for a visual aid.
                new_node.next = current_node.next # since we're moving the current node's neighbor 'up' one, that neighbor becomes the new_node's next property
                new_node.prev = current_node # Since the new node is going right in front of the current node, we set the prev property of the new node to the address of teh current node
                print("new_node.next:", new_node.next)
                new_node.next.prev = new_node # Here, we are accessing the node that is being moved 'up' to make room for the new node we are inserting.  We are changing that displaced node's prev property to reference the location of the new node we are inserting
                current_node.next = new_node # Finally, update the current node (node before the one we're inserting) to reference the newly inserted node in its next property
                return("Node with value {value} inserted in the middle of the list")
    def print_node_props(self, index, current_node):
        print("     Node Index:", index, "Node Value:", current_node.value, "Node Address:", current_node)
        if current_node.prev is None:
            print("         Prev:", current_node.prev)
        else:
            print("         Prev:", current_node.prev.value, " | ", current_node.prev)
        if current_node.next is None:
            print("         Next:", current_node.next)
        else:
            print("         Next:", current_node.next.value, " | ", current_node.next)
        print("")
    def traverse_and_print(self, direction):
        # Check to make sure the list exists:
        if self.head is None:
            print("No elements to traverse")
        # If there is more than one element, loop through and print in the direction of choice
        else:
            if direction == 'forward':
                print("Head:", self.head)
                current_node = self.head
                index = 0
                while current_node:
                    self.print_node_props(index, current_node)
                    current_node = current_node.next
                    index += 1
                print("Tail:", self.tail)
            elif direction == 'backward':
                print("Tail:", self.tail)
                current_node = self.tail
                index = 0
                while current_node:
                    self.print_node_props(index, current_node)
                    current_node = current_node.prev
                    index += 1 
            else:
                print("The direction specified is not valid, choose either: 'forward' or 'backward'")    
    def find_node_by_val(self, target_value):
        # Check to make sure the list has nodes:
        if self.head is None:
            return "There are no nodes to check"
        else:
            current_node = self.head
            while current_node:
                if current_node.value == target_value:
                    return current_node
                else:
                    current_node = current_node.next
            return "Node not found."
                


# Bookending node - The list is not very good at inferring where the end of the list aught to be.  Therefore, it is
# necessary to explictly add the final node in the list before adding elements to the middle.  Otherwise it will break.
print("CREATING NEW DLL")
print("------------------------------------------------")
my_new_dll = DoublyLinkedList()
print(my_new_dll.createDLL('A'))
print("Head:", my_new_dll.head, "Tail:", my_new_dll.tail)
print("Node Value:", my_new_dll.head.value, "Node Address:", my_new_dll.head)
print("     Prev:", my_new_dll.head.prev)
print("     Next:", my_new_dll.head.next)
print("\n"*3)
print("INSERTING NODES B-E")
print("------------------------------------------------")
print(my_new_dll.insert_node("E", -1)) # IMPORTANT!!! Read bookending node above
print(my_new_dll.insert_node("B", 1))
print(my_new_dll.insert_node("C", 2))
print(my_new_dll.insert_node("D", 3))
print("\n"*3)
print("TRAVERSING ENTIRE LIST FORWARD")
print("------------------------------------------------")
my_new_dll.traverse_and_print('forward')
print("\n"*3)
print("INSERTING NODE !!! AT POSITION 2")
print("------------------------------------------------")
print(my_new_dll.insert_node("!!!", 2))
print("\n"*3)
print("TRAVERSING ENTIRE LIST FORWARD")
print("------------------------------------------------")
my_new_dll.traverse_and_print('forward')
print("\n"*3)
print("TRAVERSING ENTIRE LIST BACKWARD")
print("------------------------------------------------")
my_new_dll.traverse_and_print('backward')
print("\n"*3)
print("SEARCHING FOR NODES D AND YYY")
print("------------------------------------------------")
print(my_new_dll.find_node_by_val("D"))
print(my_new_dll.find_node_by_val("YYY"))