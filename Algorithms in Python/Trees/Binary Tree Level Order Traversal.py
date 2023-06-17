# DFS - LEVEL ORDER TRAVERSAL
# With level order traversal, we need a LL queue as a helper data structure, so define that first.

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
        

class BinaryTreeNode:
    def __init__(self, data):
        # 'data' parameter is used to create the root node automatically when a new tree object is instantiated
        self.data = data
        self.leftChild = None
        self.rightChild = None

# First, create the nodes, starting with the root.
mybt = BinaryTreeNode("N1")
n2 = BinaryTreeNode("N2")
n3 = BinaryTreeNode("N3")
n4 = BinaryTreeNode("N4")
n5 = BinaryTreeNode("N5")
n6 = BinaryTreeNode("N6")
n7 = BinaryTreeNode("N7")
n8 = BinaryTreeNode("N8")
n9 = BinaryTreeNode("N9")
x = BinaryTreeNode("X")

# Next, assemble the tree by linking the child nodes to the root node.  
# Organized to match the diagram:  PreOrder Traversal of Binary Tree.pdf
mybt.leftChild = n2
mybt.rightChild = n3
n2.leftChild = n4
n2.rightChild = n5
n4.leftChild = n8
n4.rightChild = n9
n3.leftChild = n6
n3.rightChild = n7


# LevelOrder Traversal of Binary Tree
# Returns the values in the tree in left to right order, by level.  Note that the queue does not store data in
# distinct chunks segregrated by level.  The queue is structurally 'flat' but we achieve the behavior we want by
# starting with the root node and always adding the child nodes corresponding to the node we are dequeueing at any
# given stage. In this this way, we traverse left to right, top to bottom and return the node values in that order.
# Performs well since it uses an efficient queue data structure
# TC: O(n)
# SC: O(n)
def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        # Create a Queue object, which is used as a staging area to line nodes up for processing
        q = Queue()
        q.enqueue(rootNode) # Very first node in the queue will always be the root node
        print("Initial Queue:", q)

        while not(q.isEmpty()): # While the queue object we created is not empty
            print(" Queue:", q)
            # We can only dequeue one element at a time, but we add that node's children immediately after removing it
            # and therefore the queue will grow in size 
            root = q.dequeue()
            print("     Root:", root.value.data)
            if root.value.leftChild is not None:
                q.enqueue(root.value.leftChild) # Add the dequeued node's left child
            if root.value.rightChild is not None:
                q.enqueue(root.value.rightChild) # Add the dequeued node's right child
            
            print("         Queue:", q)
            print("")
            
print("\n"*2)
levelOrderTraversal(mybt)


# Finding a node in a binary tree
# Use LOT, since its relatively efficient
def levelOrderTraversalSearch(rootNode, target):
    if not rootNode:
        return
    else:
        q = Queue()
        q.enqueue(rootNode) 

        while not(q.isEmpty()): 
            root = q.dequeue()
            # All we gotta do is slap this if statement on the traversal method
            if root.value.data == target:
                return root
            else:
                if root.value.leftChild is not None:
                    q.enqueue(root.value.leftChild) 
                if root.value.rightChild is not None:
                    q.enqueue(root.value.rightChild) 

print("\n"*2)
result = levelOrderTraversalSearch(mybt, "N4")
print("Result:", result.value.data)
if result.value.leftChild and result.value.rightChild:
    print("Children:", "L:" + result.value.leftChild.data, "R:" + result.value.rightChild.data)