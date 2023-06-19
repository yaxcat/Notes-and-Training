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
    nodes = []
    if not rootNode:
        return
    else:
        # Create a Queue object, which is used as a staging area to line nodes up for processing
        q = Queue()
        q.enqueue(rootNode) # Very first node in the queue will always be the root node
        #print("Initial Queue:", q)

        while not(q.isEmpty()): # While the queue object we created is not empty
            #print(" Queue:", q)
            # We can only dequeue one element at a time, but we add that node's children immediately after removing it
            # and therefore the queue will grow in size 
            root = q.dequeue()
            nodes.append(root.value.data)
            #print("     Root:", root.value.data)
            if root.value.leftChild is not None:
                q.enqueue(root.value.leftChild) # Add the dequeued node's left child
            if root.value.rightChild is not None:
                q.enqueue(root.value.rightChild) # Add the dequeued node's right child
            
            #print("         Queue:", q)
            #print("")
        return ' -> '.join(nodes)    
#print("\n"*2)
#print(levelOrderTraversal(mybt))


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

#print("\n"*2)
#result = levelOrderTraversalSearch(mybt, "N4")
#print("Result:", result.value.data)
#if result.value.leftChild and result.value.rightChild:
#    print("Children:", "L:" + result.value.leftChild.data, "R:" + result.value.rightChild.data)





# Inserting a node in a binary tree
# Uses level order traversal methodology to find the first open slot to insert a node.  Since traversal is top to 
# bottom and left to right, nodes will always added to the higher, more left hand portion fo the graph first
# TC: O(n)
# SC: O(n)
def LOTInsertNode(rootNode, newNode):
    if not rootNode:
        rootNode = newNode # This doesn't actually do anything since we're not changing the tree itself
    else:
        q = Queue()
        q.enqueue(rootNode) # Add the root node to the queue so we can analyze it
        # Iterate over the tree 
        while not(q.isEmpty()):
            root = q.dequeue() # Pull the next node in line out of the queue for analysis
            
            # Handles insertion of a left child node
            if root.value.leftChild is not None: # If the current node we're looking at has a left child node
                q.enqueue(root.value.leftChild) # Add that left child to queue, so we can analyze it later
            else: # If the current node does not have a left child node
                root.value.leftChild = newNode # Add the new node as the left child node
                return f"Succesfully inserted a new left child node: {newNode.data} for parent node: {root.value.data}"
            
            # Handles insertion of a right child node
            if root.value.rightChild is not None:
                q.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return f"Succesfully inserted a new right child node: {newNode.data} for parent node: {root.value.data}"
            

# print(LOTInsertNode(mybt, x))


# Deleting a node:
# Deleting a node is tricky since the node we want to delete might have child nodes.  Therefore, we can't
# simply search for the node in question and delete it.  Instead we must replace it with another node.  We will 
# replace it with the deepest node in the graph since by definition, that node will not have any children.
#_____________________________________________________________________________________________________
# Finds the deepenest node in the graph.  This node will be swapped with the node we want to get rid of in order to
# accomplish the deletion behavior we wish for.
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        q = Queue()
        q.enqueue(rootNode)
        # Loop through the tree until there aren't any items left in queue
        while not(q.isEmpty()):
            root = q.dequeue()
            if root.value.leftChild is not None:
                q.enqueue(root.value.leftChild) 
            if root.value.rightChild is not None:
                q.enqueue(root.value.rightChild) 
        # Return the final item we dequeued, since it is the deepest node
        deepest_node = root.value
        return deepest_node
    
print("Deepest Node:", getDeepestNode(mybt).data)


# Deletes the deepest node by removing address reference
def deleteDeepestNode(rootNode, deleteNode):
    if not rootNode:
        return
    else:
        q = Queue()
        q.enqueue(rootNode)
        # Loop throught the tree until we find the node we want to delete/replace
        while not(q.isEmpty()):
            root = q.dequeue()
            
            # Deletion conditions.  Check the root itself and then both the children.  Checking the children before adding
            # them to the queue saves a bit of effort.
            if root.value is deleteNode: # If the root node is the node want to delete
                root.value = None
                return
            if root.value.rightChild: # If the root node has a right child
                if root.value.rightChild is deleteNode: # If that right child is the node we want to delete
                    root.value.rightChild = None
                    return
                else: # If its not
                    q.enqueue(root.value.rightChild) # Add the right child to the queue so we can check its children later
            if root.value.leftChild: # If the root node has a left child
                if root.value.leftChild is deleteNode: # If that left child node is the one we want to delete
                    root.value.leftChild = None
                    return
                else: # If its not
                    q.enqueue(root.value.leftChild) # Add it to the queue for subseqent analysis

#deleteDeepestNode(mybt, getDeepestNode(mybt))
#print("\n Deleting Deepest Node \n")
#print(levelOrderTraversal(mybt))
#print("Deepest Node:", getDeepestNode(mybt).data)


def deleteNodeBT(rootNode, update_node):
    if not rootNode:
        return "The binary tree does not exist"
    else:
        q = Queue()
        q.enqueue(rootNode)
        while not(q.isEmpty()):
            root = q.dequeue()
            # If we've found the node whose data we wish to update
            if root.value.data == update_node:
                deepest_node = getDeepestNode(rootNode) # Find the deepest node in the graph
                root.value.data = deepest_node.data # Update the root node's data with the data we've pulled from the deepest node (node we are going to delete)
                deleteDeepestNode(rootNode, deepest_node) # Now, delete that deepest node
                return "The node has successfully been deleted"
            
            # If we haven't found the node, enqueue its children so that we can analyze them later and keep things
            # running
            if root.value.leftChild is not None:
                q.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                q.enqueue(root.value.rightChild)
        
        # If none of that works
        return "Failed to delete the node"
    
print(levelOrderTraversal(mybt))
print("\n Deleting Deepest Node \n")
deleteNodeBT(mybt, 'N3')
print(levelOrderTraversal(mybt))
#print("Deepest Node:", getDeepestNode(mybt).data)


# All we need to do to delete the entire binary tree is sever the links between its root nodes and its children.
# Once this is done, the node itself, and (previously) subsequent nodes become eligible for garbage collection.
# TC: O(1)
# SC: O(1)
def deleteEntireBinaryTree(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The binary tree has been deleted"

