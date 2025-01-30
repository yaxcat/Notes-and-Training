#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Balanced Tree

# Check Balanced - LeetCode 110
# Implement a function to check if a binary tree is balanced. For the purposes of this question, a balanced 
# tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one.

# My Solution
# ________________________________________________________________________________________________________________
# Code passed the test, but probably isn't a great solution since the way I implemented the getLeftHeight and 
# getRightHeight functions means that I'll only get the heights of the outermost left and right boundary branches.
# there could be unblanced branches in the middle of the tree which this algorithm would miss.
class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# Create some trees
b2 = Node(2)
b6 = Node(6)
b12 = Node(12)
b18 = Node(18)
b5 = Node(5, b2, b6)
b15 = Node(15, b12, b18)
balanced = Node(10, b5, b15)


ub25 = Node(25)
ub18 = Node(18, None, ub25)
ub15 = Node(15, None, ub18)
ub5 = Node(5)
unbalanced = Node(10, ub5, ub15)


# Tracks all the way down the left edge of the tree to get the height of the outermost left branch
def getLeftHeight(root, height=0):
    if root is None:
        return 0
    else:
        height = 1 + getLeftHeight(root.left)
    return height

# Tracks all the way down the right edge of the tree to get the height of the outermost right branch
def getRightHeight(root, height=0):
    if root is None:
        return 0
    else:
        height = 1 + getRightHeight(root.right)
    return height

# Get the heights and compare them
def isBalanced(root):
    left_height =  getLeftHeight(root)
    right_height = getRightHeight(root)

    if abs(left_height - right_height) <= 1:
        return True
    else:
        return False


print("Balanced Left Height: ", getLeftHeight(balanced))
print("Balanced Right Height: ", getRightHeight(balanced))
print("Balanced?: ", isBalanced(balanced))
print("")
print("Unbalanced Left Height: ", getLeftHeight(unbalanced))
print("Unbalanced Right Height: ", getRightHeight(unbalanced))
print("Balanced?: ", isBalanced(unbalanced))
print("")
print("")
print("")


# Instructor Solution
# ________________________________________________________________________________________________________________

# He creates a helper function as well.  It recurisvely calculates the left and right height of the as long as the 
# tree is balanced.  In the event an unbalanced branch is identified, it exits.  The helper function does not suffer
# the same drawbacks as the prior solution because it is recursively called on both the left and right subtrees,
# ensuring that all the intermediate root nodes are visited and all interior branches are traversed.

def isBalancedHelper(root):
    # base case.  Hit the end of the tree where there are no nodes, so return 0
    if root is None: 
        return 0
    
    # Recursively visit every node in the tree and tabulate the height.  We can exit early if a disbalance is encountered
    leftHeight = isBalancedHelper(root.left)
    if leftHeight == -1:
        return -1
    rightHeight = isBalancedHelper(root.right)
    if rightHeight == -1:
        return -1
    if abs(leftHeight-rightHeight) > 1: # Disbalance encountered
        return -1
    
    return max(leftHeight, rightHeight) + 1 # Return the greater height, add one since each time we've hit a new node

def isBalanced2(root):
    return isBalancedHelper(root) > -1
    

print("Balanced?: ", isBalanced(balanced))
print("Balanced?: ", isBalanced(unbalanced))