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

def insertNode(rootNode, newVal):
    if not rootNode:
        return "The tree does not exist"
    if newVal < rootNode.data:
        if not rootNode.leftChild:
            rootNode.leftChild = AVLNode(newVal)
        else:
            insertNode(rootNode.leftChild, newVal)
    else:
        if not rootNode.rightChild:
            rootNode.rightChild = AVLNode(newVal)
        else:
            insertNode(rootNode.rightChild, newVal)


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
    # We must update the height of the disbalanced node to the height of its left tree or right tree, whichever is greater. We 
    # add 1 since we need to account for the disbalanced node itself too.
    disbalancedNode.height = 1 + max(getHeight(disbalancedNode.leftChild), getHeight(disbalancedNode.rightChild))
    # Need to update the height of the new root node since that also changed.  Basically the same thing.
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

#print(mybt.rightChild.rightChild.data)