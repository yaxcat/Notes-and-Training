#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# List of Depth
class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None
    
    def add(self, val):
        if self.next == None:
            self.next = LinkedList(val)
        else:
            self.next.add(val)
    def __str__(self):
        return "({val})".format(val = self.val) + str(self.next)

class BinaryTree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None



# Recursively traverses the tree to find its depth. Uses post order traversal to scan the tree 
# in a bottom to top manner where it probes all the way to the end of the tree and then starts 
# working its way back up to the root, adding 1 to the total for each node it encounters along 
# the way. Useful because there is no need for the tree to be balanced
def depth(tree):
    if tree == None: # Base case, where we have reached the very end of the tree
        return 0
    if tree.left == None and tree.right == None: # If we have reached a leaf node (bottom of the tree)
        return 1
    # If we're somewhere between the root and the leaves, traverse the left and right sides of the tree
    # by recursively calling the depth function and adding 1 at each call instance.  By returning the
    # incrementally added depth right/left with each call, we calculate the depth at a given level
    else: 
        depthLeft = 1 + depth(tree.left)
        depthRight = 1 + depth(tree.right)
        # Pick left or right, whichever is greater
        if depthLeft > depthRight:
            return depthLeft
        else:
            return depthRight
        
# Builds a dictionary of linked lists representing nodes at each depth level of the tree.
# The function first determines the depth of the tree and then uses a helper dictionary to
# store nodes at each depth level. Nodes are added to the linked lists in a manner resembling
# pre-order traversal but with depth-specific organization.
def treeToLinkedList(tree, custDict = {}, d = None):
    # Initially the depth parameter will be none, so we must run the helper function find the depth
    if d == None:
        d = depth(tree)
    # If there is no dictionary item for the current depth, create one and add the current node's
    # value as a linked list object
    if custDict.get(d) == None:
        custDict[d] = LinkedList(tree.val)
    # Otherwise, add the node to the existing linked list
    else:
        custDict[d].add(tree.val)
        # If our depth is 1, we've reached the last level of the tree, so return the dictionary and
        # we're done
        if d == 1: # Base case
            return custDict
    # Recursively traverse the left and right sides of the tree to build out the linked lists.  Since
    # we're immediately returning the linked list node and appending it to the dict with each fn call
    # this is pre-order traversal
    if tree.left != None:
        custDict = treeToLinkedList(tree.left, custDict, d-1)
    if tree.right != None:
        custDict = treeToLinkedList(tree.right, custDict, d-1)
    return custDict


n2 = BinaryTree(2)
n3 = BinaryTree(3)
n12 = BinaryTree(12)
n18 = BinaryTree(18)
n5 = BinaryTree(5)
n15 = BinaryTree(15)
root = BinaryTree(10)

n5.left=n2
n5.right=n3
n15.left=n12
n15.right=n18
root.left=n5
root.right=n15

my_dict = treeToLinkedList(root)

for depthLevel, linkedList in my_dict.items():
    print("{0} {1}".format(depthLevel, linkedList))