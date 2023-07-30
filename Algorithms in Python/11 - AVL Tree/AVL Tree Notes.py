# AVL TREE

# An AVL tree is a self-balancing binary search tree, where the difference between left and right subtree
# heights cannot be more than one for all nodes.

# Any time the height of the left and right subrees differ by more than one, rebalancing will occur, and this
# process is called 'rotation'

# Utility:
#   Unbalanced binary search trees can get really long on either the right or left subtree.  If the number
#   of nodes is heavily biased to one side or the other, we lose much of the benefit of binary tree for most
#   operations.  The more 'linear' a tree starts to look, the more operational time compexity will tend towards
#   O(n), instead of O(logN).  Performance of a binary tree is tied to the height of the tree.

# For AVL tree node insertion, one of two scenarios will be true:
#   1. Rotation (balancing) is not required
#   2. Rotation (balancing) is required
#       a.  left left condition (LL) - Rotate right       
#       b.  left right condition (LR) - Rotate left, then right
#       c.  right right condition (RR) - Rotate left
#       d.  right left condition (RL) - Rotate right, then left
# 
# See diagrams for more details

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

def preOrderTraversal(rootNode, tr=[]):
    if not rootNode:
        return 
    tr.append(str(rootNode.data))
    preOrderTraversal(rootNode.leftChild, tr)
    preOrderTraversal(rootNode.rightChild, tr)
    return tr

def inOrderTraversal(rootNode, tr=[]):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftChild, tr)
    tr.append(str(rootNode.data))
    inOrderTraversal(rootNode.rightChild, tr)
    return tr

def postOrderTraversal(rootNode, tr=[]):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftChild, tr)
    postOrderTraversal(rootNode.rightChild, tr)
    tr.append(str(rootNode.data))
    return tr

import QueueHelper as qh
def levelOrderTraversal(rootNode):
    traversal_result = []
    q = qh.Queue()
    q.enqueue(rootNode)
    while q.isEmpty() is False:
        root = q.dequeue()
        traversal_result.append(root.value.data)
        if root.value.leftChild is not None:
            q.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            q.enqueue(root.value.rightChild)
    return traversal_result

# TC: O(logN) since we're halving the search area each time
def searchNode(rootNode, searchVal):
    if rootNode.data == searchVal:
        return "Node found at root: " + searchVal
    else:
        if searchVal < rootNode.data:
            if rootNode.leftChild.data == searchVal:
                return "Node found on left: " + searchVal
            else:
                searchNode(rootNode.leftChild, searchVal)
        else:
            if rootNode.rightChild == searchVal:
                return "Node found on right: " + searchVal
            else:
                searchNode(rootNode.rightChild, searchVal)

def getHeight(rootNode):
    if not rootNode:
        return 0
    else:
        return rootNode.height

# TC: O(1)
# SC: O(1)
# See AVL LL diagram for visual description
def rotateRight(disbalancedNode):
    # The left child of the disbalanced node becomes the root because its value is less than the disbalanced node but greater
    # its own left child (the left granchild of the disbalanced node)
    newRoot = disbalancedNode.leftChild 
    # The left child of the disbalanced node is now replaced with the right child of the disbalanced node's leftchild because 
    # that node is guaranteed to be less than the value of the disbalanced node, but greater than the value of the leftchild. 
    # Therefore, it cannot possibly conflict (be greater than) the disbalanced node's existing right node  
    disbalancedNode.leftChild = disbalancedNode.leftChild.rightChild
    newRoot.rightChild = disbalancedNode
    # We must update the height of the disbalanced node to the height of its left tree or right tree, whichever is greater. We 
    # add 1 since we need to account for the disbalanced node itself too.
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    # Need to update the height of the new root node since that also changed.  Basically the same thing.
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot


# TC: O(1)
# SC: O(1)
# See AVL RR diagram for visual description
def rotateLeft(disbalancedNode):
    # The right child of the disbalanced node becomes the new root because it is greater than the disbalanced node but less
    # than its right child, which allows it to have both a left and right child, after we perform the rotation
    newRoot = disbalancedNode.rightChild
    # The disbalanced node's right child is set to its right child's left child because that value will be gauranteed to be
    # greater than the disbalanced node, but less than the right child itself.  Because its also guranteed to be greater than
    # the disbalanced node's existing left child, it can slide right into the open right child spot without causing any
    # problems
    disbalancedNode.rightChild = disbalancedNode.rightChild.leftchild
    # Update the new root's left child to point to the disbalanced node, because that node is smaller than the new root.  Note
    # how the new right child (disbalanced node) child references carry right over and the correct shape is formed.  Very clever
    newRoot.leftChild = disbalancedNode
    # We must update the height of the disbalanced node to the height of its left tree or right tree, whichever is greater. We 
    # add 1 since we need to account for the disbalanced node itself too.
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    # Need to update the height of the new root node since that also changed.  Basically the same thing.
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

# TC O(1)
# SC O(1)
# Subtracts the height of the right subtree from that of the left subtree in order to find the balance
def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

# TC O(logN) - due to the recursive function calls
# SC O(logN) - due to the recursive function calls
def insertNode(rootNode, nodeValue):
    # if the tree is empty, create a root node
    if not rootNode:
        return AVLNode(nodeValue)
    # If the node value we wish to insert is less than the root node, call the insert function recursively until we find a spot to
    # insert it
    elif nodeValue < rootNode.data:
        rootNode.leftChild = insertNode(rootNode.leftChild, nodeValue)
    # If the value for the node we wish to insert is greater than the root node, recursively call the insert function until we find
    # the insertion point
    else:
        rootNode.rightChild = insertNode(rootNode.rightChild, nodeValue)
    # Update the height of the root node to account for the fact that we inserted a new node.  The height of the root will be 1 plus
    # the height of the left subtree or the right subtree, whichever is greater.
    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    # Get the balance to understand if we we need to rotate the nodes.  We know that any time we have a balance of greater than 1,
    # rotation is required.  
    balance = getBalance(rootNode)
    # LL condition - if the node we wish to insert is less than the left child of the root node.  We know this because if it is
    # we effectively have 'three left node's in a line', which is no good.
    if balance > 1 and nodeValue < rootNode.leftChild.data:
        return rotateRight(rootNode)
    # LR condition - if the node we're inserting is greater than the value of the root node's left child
    if balance > 1 and nodeValue > rootNode.leftChild.data:
        # First rotate left.  We're passing in the 'middle node' between the root and disbalanced right child here because when we
        # do, we effectively cause the root's left child and the left childs right child to swap places.  That gives us a nice line
        # of left nodes (LL condition) to work with
        rootNode.leftChild = rotateLeft(rootNode.leftChild)
        # Now all we have to do is take that chain of three nodes and rotate it right
        return rotateRight(rootNode)
    # RR condition - if the node we're inserting is greater than the right child of the root node.  A negative balance indicates that
    # the right side is bigger
    if balance < -1 and nodeValue > rootNode.rightChild.data:
        return rotateLeft(rootNode)
    # RL condition - if the node were inserting is less than the right child of the root node
    if balance < -1 and nodeValue < rootNode.rightChild.data:
        # First rotate right.  Passing in the right child of the root as our disbalanced node causes the rotateRight() function to flip
        # the position of the right child and its left child.  What we get is a nice even line down the right side (RR condition), which 
        # is exactly what we want.
        rootNode.rightChild = rotateRight(rootNode.rightChild)
        # Then rotate left
        return rotateLeft(rootNode)
    

# Returns the minimum value of an AVL tree.  Necessary because when deleting a node with two children, we need to find a successor,
# which can take the deleted node's place.  The successor is the minimum node in the right subtree since that node is greater than
# all values on the left subtree, but also less than all values on the right subtree.  This property allows it to slide right into
# the spot previously occupied by the deleted node.
def getMinValueNode(rootNode):
    # If there is no root, or if we have reached the end of the left subtree, return the root node.  This will be the minimum value
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    # if the tree has multiple nodes, recursively call the function so that we traverse the entire left side of the tree from the 
    # root node down
    return getMinValueNode(rootNode.leftChild)

# TC: O(logN)
# SC: O(logN) - due to the call stack
def deleteNode(rootNode, nodeValue):
    # Base case
    if not rootNode:
        return rootNode
    # Rotation is not required________________________________________________________________________________________________________
    # Look for the node by recursively calling the function on the right or left subtree depending on the value of the node we wish to 
    # delete
    elif nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild, nodeValue) # Assign the root node's left child the returned temp value
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild, nodeValue) # Assign the root node's right child the returned temp value
    # Once we have found the node we wish to delete
    else:
        # If we want to delete a node which has a right child
        if rootNode.leftChild is None:
            temp = rootNode.rightChild # The right child might have a value or it might be null.  If right child has a value, it is a leaf node, if right child is also None, than the root is a leaf node
            rootNode = None # Delete the target node
            return temp # Returning temp will cause it to replace the target node we just deleted via the recursive function calls above
        elif rootNode.rightChild is None:
            temp = rootNode.leftChild # The left child might have a value or it might be null.  If left child has a value, it is a leaf node, if left child is also None, than the root is a leaf node
            rootNode = None # Delete the target node
            return temp # Returning temp will cause it to replace the target node we just deleted via the recursive function calls above
        
        # If the node we wish to delete has two children, we have to identify the successors
        successor = getMinValueNode(rootNode.rightChild) # Use this function to ID the successor node
        rootNode.data = successor.data # In order to accomplish the delete, replace the root node's data with that of the successor node
        rootNode.rightChild = deleteNode(rootNode.rightChild, successor.data) # Now we must delete the original successor node, so call the delete function recursively
    # Now check to see if we need to perform an rotations
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0: # LL condition
        return rotateRight(rootNode) # All we need to do is rotate right
    if balance < -1 and getBalance(rootNode.rightChild) <= 0: # RR condition
        return rotateLeft(rootNode) # All we need to do is rotate left
    if balance > 1 and getBalance(rootNode.leftChild) < 0: # RL condition - Perform a right rotation on the left child
        rootNode.leftChild = rotateLeft(rootNode.leftChild)
        return rotateRight(rootNode) 
    if balance < -1 and getBalance(rootNode.rightChild) > 0: #LR condition - Perform a left rotation on the right child
        rootNode.rightChild = rotateRight(rootNode.rightChild)
        return rotateLeft(rootNode)
    
    return rootNode

# TC: O(1)
# TC: O(1)
def deleteAVLTree(rootNode):
    rootNode.data = None
    rootNode.rightChild = None
    rootNode.rightChild = None
    return "The AVL tree was successfully deleted"
