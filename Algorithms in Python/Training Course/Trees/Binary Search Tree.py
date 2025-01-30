# BINARY SEARCH TREE

# Structure:
#   - In the left subtree, the value of a node is always less than or equal to its parent node's value
#   - In the right subtree, the value of a node is always greater than its parent node's value
#   - Does not store an index of elements, but instead relies on its implicit structure to keep track of where
#     things are

# Advantages:
#   1.  Insertion and deletion is very quick.  Instead of needing to traverse the entire object to get to a value
#       we can just traverse half the tree, then half again, half again, etc.


# Note how this is identical to the node structure of other binary trees we've created.  Nothing special yet.
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None


# TC: O(logN)
# SC: O(logN)
def insertNode(rootNode, nodeValue):
    # If the root doesn't have a value, assign it the value of whatever we passed in
    if rootNode.data == None:
        rootNode.data = nodeValue
    # If the value we're trying to insert is less than the value of the root node    
    elif nodeValue <= rootNode.data:
        # If the root node doesn't have a left child
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue) # Just create a new node with the value we passed in and bind it to the root as the left child
        # If the root does have a left child
        else:
            insertNode(rootNode.leftChild, nodeValue) # Call the function recursively so that we can traverse the tree until we find an open spot
    # If the value we're trying to insert is greater than that of the root node
    else:
        # If the root node doesn't have a right child
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        # If it does
        else:
            insertNode(rootNode.rightChild, nodeValue) # Call the function recursively until we can find a spot to insert the value

# TC: O(n)
# SC: O(n)
def preOrderTraversal(rootNode, traversal_result=[], side="-"):
    # Exit condition where the child is null
    if not rootNode:
        print(f"    {side} - Exit")
        return
    traversal_result.append(rootNode.data) # First, we process the root node
    print("Side:", side, "Node:", rootNode.data, traversal_result)
    preOrderTraversal(rootNode.leftChild, traversal_result, "L") # Next we will recursively run the function until we run out of left children
    preOrderTraversal(rootNode.rightChild, traversal_result, "R") # Finally, we will recursively run the function call until we run out of right children
    return traversal_result


# TC: O(n)
# SC: O(n)
def inOrderTraversal(rootNode, traversal_result=[], side="-"):
    # Exit condition
    if not rootNode:
        print(f"    {side} - Exit")
        return # If we've run out of nodes, just exit
    inOrderTraversal(rootNode.leftChild, side="L") # Recursively run the function until we hit the deepest unvisited left node (leaf)
    print("Side:", side, "Node:", rootNode.data, traversal_result)
    traversal_result.append(rootNode.data) # Add whatever the unprocessed root node (left or right) is the list
    inOrderTraversal(rootNode.rightChild, side = "R") # Recursively run the function until we hit the deepest unvisited right node
    return traversal_result

def postOrderTraversal(rootNode, traversal_result=[], side="-"):
    # Exit condition
    if not rootNode:
        print(f"    {side} - Exit")
        return # None result signifies that the left/right child does not exist and we have therefor run out of nodes in the branch
    postOrderTraversal(rootNode.leftChild, side="L") # Recursively run the function until we hit the deepest node on the left side, then start coming back up
    postOrderTraversal(rootNode.rightChild, side="R") # Recursively run the function until we hit the deepest node on the right side, then start coming back up
    traversal_result.append(rootNode.data) # Then process whatever our current node is
    print("Side:", side, "Node:", rootNode.data, traversal_result)
    return traversal_result

# Level Order Traversal (breadth first) requires a queue data structure when implemented with linked list
import LinkedLIstQueue as q

def levelOrderTraversal(rootNode):
    traversal_result = []
    if rootNode is None:
        return "There is no list to traverse"
    queue = q.LinkedListQueue() # Create the queue object, which will serve as a staging area
    queue.enqueue(rootNode) # Add the very first node to the queue
    while not(queue.isEmpty()): # As long as the queue isn't empty...
        root = queue.dequeue() # Dequeue the first item in the queue and access its properties.  Queues are FIFO
        if root.value.leftChild is not None:
            queue.enqueue(root.value.leftChild) # Add the current node's left child, if it exists
        if root.value.rightChild is not None:
            queue.enqueue(root.value.rightChild) # Add the current node's right child, if it exists
        traversal_result.append(root.value.data) # Process the current node, before its thrown away
    return traversal_result



mybst = BSTNode(70)
insertNode(mybst, 50)
insertNode(mybst, 90)
insertNode(mybst, 30)
insertNode(mybst, 60)
insertNode(mybst, 80)
insertNode(mybst, 100)
insertNode(mybst, 20)
insertNode(mybst, 40)

print("")
print(levelOrderTraversal(mybst))