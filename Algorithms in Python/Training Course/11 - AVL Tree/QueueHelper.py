class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
class Queue:
    def __init__(self):
        self.linked_list = LinkedList()

    def isEmpty(self):
        if self.linked_list.head is None:
            return True
        return False
    
    def __str__(self):
        nodes = [str(x.value.data) for x in self.linked_list]
        return '->'.join(nodes)
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.linked_list.head is None:
            self.linked_list.head = new_node
            self.linked_list.tail = new_node
        else:
            self.linked_list.tail.next = new_node
            self.linked_list.tail = new_node

    def dequeue(self):
        if self.linked_list.head is None:
            return "There are no nodes in the list"
        else:
            if self.linked_list.head == self.linked_list.tail:
                return_val = self.linked_list.head
                self.linked_list.head = None
                self.linked_list.tail = None
                return return_val
            else:
                return_val = self.linked_list.head
                self.linked_list.head = self.linked_list.head.next
                return return_val
    
    def peek(self):
        if self.isEmpty() == True:
            return "The list is empty, there are no nodes to peek at."
        else:
            return self.linked_list.head