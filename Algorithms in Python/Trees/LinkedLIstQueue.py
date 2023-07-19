class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
    
    def __str__(self):
        return f"{self.value}"

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next



# Queue stuff
class LinkedListQueue:
    def __init__(self):
        self.ll = LinkedList()

    def isEmpty(self):
        if self.ll.head is None:
            return True
        else:
            return False

    def __str__(self):
        nodes = [str(node) for node in self.ll]
        #first_to_last = reversed(nodes)
        return ' -> '.join(nodes)
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.ll.head is None:
            self.ll.head = new_node
            self.ll.tail = new_node
        # Since this is a queue, new nodes will be added at the end
        else:
            self.ll.tail.next = new_node
            self.ll.tail = new_node

    def dequeue(self):
        if self.isEmpty() == True:
            return "The list is empty, there are no elements to dequeue."
        else:
            # If there is only one node in the list
            if self.ll.head == self.ll.tail:
                removed_node = self.ll.head
                self.ll.head = None
                self.ll.tail = None
                return removed_node
            # If there is more than one node in the list
            else:
                removed_node = self.ll.head
                self.ll.head = self.ll.head.next
                return removed_node
    def peek(self):
        if self.isEmpty() == True:
            return "The list is empty, there are no nodes to peek at."
        else:
            return self.ll.head
    
    def delete_entire_queue(self):
        self.ll.head = None
        self.ll.tail = None