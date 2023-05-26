# CIRCULAR SINGLY LINKED LISTS

# Node class is identical to the regular singly linked list
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
# Circular LL class is also identical to its regular counterpart
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.list_len = 0

    # Method to create a circular SLL.
    def create_CSLL(self, node_value):
        node = Node(node_value) # Set the node value to whatever we passed in
        node.next = node # Since we're creating a new CSLL, we know there is only one node, and that node's next property must be set to its own location
        self.head = node # Since there is only one node, set both head and tail to its location
        self.tail = node
        self.list_len += 1
        return f"Circular SLL created with a single node value: {node.value} at location: {node}"
    
    # Method to insert nodes:
    def insert_CSLL_node(self, value, location):
        # Check to see if the list exists
        if self.head is None:
            return "The list does not exist"
        else:
            new_node = Node(value)
            # If we want to insert the node at the beginning of the list:
            if location == 0:
                new_node.next = self.head # Set the next node value of the node we're inserting to that of the current first node
                self.head = new_node # Update the head to reference our newly inserted node location
                # ADDITIONAL STEP FOR CSLL - Update last to first link
                self.tail.next = new_node # Tail's next property is the first node in the list, since its circular
            # If we want to add a node at the end of the list:
            elif location == -1:
                new_node.next = self.tail.next # Link our (new and not yet inserted) last node to the first node in the list
                self.tail.next = new_node # Set the current last node's next property to be the location of the new last node we are inserting
                self.tail = new_node # Set tail to the location of our new last node
            # If we want to insert a node into the middle of the list:
            else:
                current_node = self.head # Start at the head to begin traversal
                index = 0 
                print("Head:", current_node)
                print("")
                print("     Entering While Loop----------------")
                while index < location -1: # Loop will terminate two nodes before our destination
                    print("     Index:", index)
                    print("         Current Node Value:", current_node.value, "| Current Node Address:", current_node)
                    print("             Next Node Value:", current_node.next.value, "| Next Node Address:", current_node.next)
                    current_node = current_node.next 
                    index += 1
                print("     Exited While Loop------------------")
                print("")
                print("Prior to Updating:")
                print(" Index:", index)
                print("     Current Node Value:", current_node.value, "| Current Node Address:", current_node)
                print("         Next Node Value:", current_node.next.value, "| Next Node Address:", current_node.next)
                next_node = current_node.next
                current_node.next = new_node
                new_node.next = next_node
                print(" After Updating:")
                print("     Current Node Value:", current_node.value, "| Current Node Address:", current_node)
                print("         Next Node Value:", current_node.next.value, "| Next Node Address:", current_node.next)
                # Added just in case we insert a node at the end of the list without using a -1
                if new_node.next == self.head:
                    self.tail = new_node
            self.list_len += 1
            return "Node Successfully Inserted"
    def traverse_and_print(self):
        if self.list_len == 0:
            print("The list is empty")
            print("Head:", self.head)
            print("Tail:", self.tail)
        else:
            current_node = self.head
            index = 0
            print("Head:", current_node)
            while current_node.next != self.head:
                print(" Index:", index)
                print("     Current Node Value:", current_node.value, "| Current Node Address:", current_node)
                print("         Next Node Value:", current_node.next.value, "| Next Node Address:", current_node.next)
                current_node = current_node.next
                index += 1
            print(" Index:", index)
            print("     Current Node Value:", current_node.value, "| Current Node Address:", current_node)
            print("         Next Node Value:", current_node.next.value, "| Next Node Address:", current_node.next)
            print("Tail:", self.tail)
    def find_val(self, target_value):
        # Check to see if there are even nodes to search
        if self.head is None:
            return "There are no nodes to search"
        else:
            node = self.head
            # Loop through all nodes and see if we can find the value we are looking for
            while node.next != self.head: # Terminate at the end of the list, rather than looping forever
                if node.value == target_value:
                    return node
                node = node.next
            return "The node value you are looking for was not found"
    def delete_node_by_position(self, position):
        # Check to see if there are even nodes to delete
        if self.head is None:
            return "There are no nodes to delete"
        else:
            if position == 0: # If we're deleting the first node
                if self.head == self.tail: # If there is only one element in the list
                    # Set head, tail and node.next to None to enable garbage collection
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else: # If there is more than one element
                    self.head = self.head.next # Set the head value to the second node in the list
                    self.tail.next = self.head # Because this is a circular LL, update the last node in the list with address of the new first node
                self.list_len -= 1
                return "First node deleted"
            if position == -1: # If we're deleting the last node
                if self.list_len == 1:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else: # if there is more than one element, we need to loop
                    current_node = self.head
                    while current_node.next != self.tail: # Terminate one node before the tail
                        current_node = current_node.next # Advance through the list
                    # Since the second to last node will now be the last node and this is a CSLL, update our new terminal node with the address of teh first node in the list
                    current_node.next = self.head
                    self.tail = current_node # Update the tail to reflect the new last node address
                self.list_len -= 1
                return "Last node deleted"
            else: # If we're deleting a node from somewhere in the middle of the list
                current_node = self.head
                index = 0
                while index < position - 1: # Treverse until the element before the element we want to delete 
                    current_node = current_node.next 
                    index += 1 # Advance through the list
                deletion_node = current_node.next # Node we want to delete
                current_node.next = deletion_node.next # Set the current node's next property to the node AFTER the one we're deleting
                self.list_len -= 1
                return "Middle node deleted"                




print("CREATING NEW CSLL")
print("------------------------------------------------")
my_csll = CircularSinglyLinkedList() # Create an instance of the class
print(my_csll.create_CSLL('A')) # Call the method to create a list
my_csll.insert_CSLL_node("B", 1)
my_csll.insert_CSLL_node("C", 2)
my_csll.insert_CSLL_node("D", 3)
my_csll.insert_CSLL_node("E", -1)
print("List Length:", my_csll.list_len)
print("\n"*3)
print("TRAVERSING ENTIRE LIST")
print("------------------------------------------------")
my_csll.traverse_and_print()
print("\n"*3)
print("DELETING NODE FROM START OF LIST")
print("------------------------------------------------")
print(my_csll.delete_node_by_position(2))
print("\n"*3)
print("TRAVERSING ENTIRE LIST")
print("------------------------------------------------")
my_csll.traverse_and_print()