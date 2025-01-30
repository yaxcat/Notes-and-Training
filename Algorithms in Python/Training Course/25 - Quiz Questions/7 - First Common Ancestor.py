#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# First Common Ancestor

# First Common Ancestor - LeetCode 236
# Design an algorithm and write code to find the first common ancestor of two nodes in 
# a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not 
# necessarily a binary search tree.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def findNode(target, root):
    # Base case - if the current node is none, the target was not found in this subtree
    if not root:
        return False
    # If we've found the node, return true, otherwise run the function recursively on the 
    # right and left subtrees
    if target == root:
        return True
    else:
        # Will return true if the target is found on the right or left branch
        return (findNode(target, root.left) or findNode(target, root.right))


def findFirstCommonAncestor(n1, n2, root):
    # First, we need to establish if the two nodes exist in the same branch that stems from
    # the root (same side of the tree).  The choice of left vs. right is arbitrary.  Either
    # will work here.
    n1_OnLeft = findNode(n1, root.left)
    n2_OnLeft = findNode(n2, root.left)

    # The 'exclusive or operator (^) is used here because while it returns true if a is true
    # and b is false, it will return false if a and b are both true.  This is what we want
    # because in the event that both our target nodes are on the same side of the tree, we
    # want to run the function recursively, but if one target is on the left and the other is
    # on the right, we need to return their parent (root) node because we've found what we're
    # looking for
    if n1_OnLeft ^ n2_OnLeft:
        return root
    # Recursively look for the nodes.  If N1 is on the left branch look there, if its on the
    # right, traverse that branch.
    else:
        if n1_OnLeft:
            return findFirstCommonAncestor(n1, n2, root.left)
        else:
            return findFirstCommonAncestor(n1, n2, root.right)



n54 = Node(54)
n33 = Node(33)
n35 = Node(35)
n88 = Node(88, n54)
n90 = Node(90, None, n33)
n95 = Node(95)
n22 = Node(22, n35, n88)
n99 = Node(99, n90, n95)
n44 = Node(44, n22, n99)
n77 = Node(77)
root = Node(55, n44, n77)


test = findFirstCommonAncestor(n35, n77, root)
print(test.value)

