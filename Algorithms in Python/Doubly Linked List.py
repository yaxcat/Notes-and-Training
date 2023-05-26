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
    


print("CREATING NEW DLL")
print("------------------------------------------------")
my_new_dll = DoublyLinkedList()
print(my_new_dll.createDLL('A'))
print("Head:", my_new_dll.head, "Tail:", my_new_dll.tail)
print("Node Value:", my_new_dll.head.value, "Node Address:", my_new_dll.head)
print("     Prev:", my_new_dll.head.prev)
print("     Prev:", my_new_dll.head.next)
print("\n"*3)