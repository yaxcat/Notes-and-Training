#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Validate BST

# Validate BST - LeetCode 98
# Implement a function to check if a binary tree is a Binary Search Tree.

class TreeNode:
     def __init__(self, value):
         self.val = value
         self.left = None
         self.right = None


# Easiest to do with a helper function
def isValidHelper(node, minVal=float('-inf'), maxVal=float('inf')):
    # Base case, if we've reached the end of the tree, just return true
    if not node:
        return True
    
    nodeVal = node.val

    # The node value should be between the minimum and maximum allowed values.  If
    # it isn't, it means the BST property has been violated
    if nodeVal <= minVal or nodeVal >= maxVal:
        return False

    # Recursively call the function on left and right subtrees
    if not isValidHelper(node.right, nodeVal, maxVal): # Right subtree first
        return False # If the if block above evaluated by the function call here evaluates to false, return false, otherwise walk the tree
    if not isValidHelper(node.left, minVal, nodeVal): # Left subtree
        return False
    
    return True

def isValidBST(root):
    return isValidHelper(root)





tn1 = TreeNode(1)
tn4 = TreeNode(4)
trueBST = TreeNode(2)
trueBST.left = tn1
trueBST.right = tn4

fn2 = TreeNode(2)
fn5 = TreeNode(5)
fn3 = TreeNode(3)
fn3.left = fn2
fn3.right = fn5
fn1 = TreeNode(1)
falseBST = TreeNode(4)
falseBST.left = fn1
falseBST.right = fn3


print(isValidBST(trueBST))


    # If the current root node has a right or left child, compare its value
    # against that of its child.  If BST relationship is maintained in this 
    # instance, keep calling the validation function until we run out of
    # nodes.  If it is violated, return false