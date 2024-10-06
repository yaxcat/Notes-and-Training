#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# In-order Successor in BST - LeetCode 285
# Write an algorithm to find the next node (i.e in-order successor) of 
# given node in a binary search tree. You may assume that each node has 
# a link to its parent.

class Node: 
	def __init__(self, key): 
		self.data = key 
		self.left = None
		self.right = None

def insert(node, data):
   if node is None:
       return Node(data)
   else:
       if data <= node.data:
           temp = insert(node.left, data)
           node.left = temp
           temp.parent = node
       else:
           temp = insert(node.right, data)
           node.right = temp
           temp.parent = node      
       return node
   

# Instructor's solution. Implementation is more complex; relies on the node's
# parent property
# ________________________________________________________________

# Gets the minimum node value in a given subtree
def minValue(node):
    current = node
    # Loop through the tree until we find the leftmost leaf
    while current is not None:
        if current.left is None:
            break
        current = current.left
    return current

def inOrderSuccessor2(root, target):
    # Because we know that in order traversal operates from L -> Rt -> R, we know
    # that as long as there is a right node, if we traverse its left branch all
    # way to the bottom to find its left-most leaf, that leaf node is the successor
    # In other words, if the target node has a right child, the successor is the leftmost node
    # in the right subtree (smallest node in the right subtree)
    if target.right is not None:
        return minValue(target.right)

    # If the target's sucessor is null, it means the we need to navigate back up the
    # tree to look for an ancestor.
    parent = target.parent 
    # Walk back up to the top of the tree until we find the first node that is the right
    # child of our target's parent
    while parent is not None:
        # If the target is not the right child of its parent, it means we've found 
        # our successor node (the parent's parent), which will be as leftward as possible
        #  This will happen when we walk up the tree
        if target != parent.right: 
            break
        target = parent # Move up the tree to the target's parent
        parent = parent.parent # Go another level up the tree
    return parent



   
# My solution.  Seems to work, but did not pass the automated test.
# ________________________________________________________________

# Relies on a helper function, which performs in-order traversal to build out and return
# a list of the nodes in the tree
def helper(root, nodes=[]):
    if root is None:
        return None
    helper(root.left)
    nodes.append(root)
    helper(root.right)
    return nodes

# Then the list is traversed.  If the target node is found, the function will just return
# the next node in the list, as long as the target is not the final node in the list
def inOrderSuccessor(root, n):
    nodes = helper(root)
    num_nodes = len(nodes)

    for node in nodes:
        print(node.data)

    for i in range(0, num_nodes):
        if nodes[i].data == n:
            if i < num_nodes-1:
                return nodes[i+1].data
            else:
                return None
    return None




bst = Node(4)
insert(bst, 2)
insert(bst, 8)
insert(bst, 1)
insert(bst, 3)
insert(bst, 5)
insert(bst, 9)

# My solution
print("")
print("")
print("***", inOrderSuccessor(bst, 3))

# Instructor's solution
print("")
print("")
test_node = bst.left.right # Using the node with a value of 3 as our test case
successor = inOrderSuccessor2(bst, test_node)
if successor is not None:
    print(test_node.data, successor.data)
else:
    print("There is no successor")


