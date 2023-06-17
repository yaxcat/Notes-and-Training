# TREES

# A tree is a non-cyclical, non-linear data structure with heirarchical relationships between its elements.  It
# looks like an upsidedown tree canopy, or roots, if you will.  Contrast this with arrays, stacks, queues and linked
# lists which are linear data structures which store data sequentially.

# Properties of tree data structures:
#___________________________________
#   1. Represent heirarchical relationships - each level down is a more specialized version of the parent
#   2. Every node has two components:
#       a. Data - stores the information we care about
#       b. Link to its subcategory - stores addresses (physical location in memory)
#   3. There is a single base category that contains all subcategories.  The number of subcategories is unlimited
#

# Utility of tree data structures:
# _______________________________
# In order to store/manipulate data in a linear data structure like an array or linked list, the computational 
# complexity increases linearly with the amount of data stored.  This is not always acceptable.  Specific reasons
# to use trees include:
#   1. Quicker, easier access to the data
#   2. Storing naturally heirarchical data like a folder structure
#   3. Many varuations of tree data structures exist for different use cases

# Tree terminology:
# _________________
#   1. Root - A node without any parent (i.e. the first node)
#   2. Edge - A link between parent and child node
#   3. Leaf - A childless node (i.e. an end node)
#   4. Sibling - If two nodes eminate from the same parent, they are siblings 
#   5. Ancestor - Nodes linked to but upstream of the node in question
#   6. Depth of node - The length of the path from the root to the node in question
#   7. Height of node - The length of the path from the node in question to the deepest node on that branch
#   8. Depth of tree - Depth of the of the root node (always 0)
#   9. Height of tree - Number of edges between the root node and the deepest node in the tree


# Creating a simple tree
#_____________________________________________________________________________________________________________

class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = "   " * level + str(self.data)  + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

# Create the root node
tree = TreeNode("Drinks", [])
#print(tree)

# Create what will be the child nodes
cold = TreeNode("Cold", [])
hot = TreeNode("Hot", [])
coffee = TreeNode("Coffee", [])
tea = TreeNode("Tea", [])

# Add the children to the root
tree.addChild(cold)
tree.addChild(hot)
hot.addChild(coffee)
hot.addChild(tea)

#print(tree)



# Binary Trees
#_____________________________________________________________________________________________________________
# In a binary tree, each node may only have a maximum of two children, which are often referred to as left and
# right.

# Types of binary tree:
#   1. Full Binary Tree - each node has either 0 or 2 children
#   2. Perfect Binary Tree - all non-leaf nodes have 2 children and all leaf nodes are at the same level. The 
#      number of nodes doubles for each level in the tree
#   3. Complete Binary Tree - each level except the final level is filled (i.e. parents nodes on all levels
#      preceeding the final level have two child nodes).  The final level need not be full, but any leaf nodes
#      must be at the extreme left of the graph.
#   4. Balanced Binary Tree - all leaf nodes are the same number of levels from the root node.
#

# Binary trees form the basis of more advanced data structures:
#   1. Binary search tree
#   2. Heap tree
#   3. AVL
#   4. Red black trees
#   5. Syntax tree

# Binary trees can be created with a linked list or Python list

# Traversal:
#   1. Depth first search
#      - PreOrder Traversal: Root node, left subtree, right subtree
#
#
#
#   Breadth first search
#
#

# DFS - PreOrder Traversal
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



# We can now define a function to perform pre-order traversal
# TC: O(n),
# SC: O(n) since we're using stack memory
def preOrderTraversal(rootNode, node_returns=[], side=None):
    if not rootNode:
        print("     " + (" -> ".join(node_returns)))
        return 
    # Added this section to help understand the recursive flow
    if side == 'Left':
        print("L: ", rootNode.data)
    elif side == 'Right':
        print("R:", rootNode.data)
    else:
        print("-:", rootNode.data)
    node_returns.append(rootNode.data)
    preOrderTraversal(rootNode.leftChild, node_returns, side='Left') # Function calls itself recursively until it runs out of left nodes
    preOrderTraversal(rootNode.rightChild, node_returns, side='Right') # Then, the same thing happens until we run out of right nodes
    print("")

print("PREORDER TRAVERSAL")
preOrderTraversal(mybt)



# In order traversal function
# Notice how the code is basically identical to the preOrderTraversal function.  Traversal of the graph takes place
# in exactly the same order as the function.  The difference in output is simply due to where the print statements
# are located.
# TC: O(n)
# SC: O(n)
def inOrderTraversal(rootNode,node_returns=[], side=None):
    if not rootNode:
        print("     " + (" -> ".join(node_returns)))
        return
    node_returns.append(rootNode.data)
    inOrderTraversal(rootNode.leftChild, node_returns, side="Left")
    if side == 'Left':
        print("L: ", rootNode.data)
    elif side == 'Right':
        print("R:", rootNode.data)
    else:
        print("-:", rootNode.data)
    inOrderTraversal(rootNode.rightChild, node_returns,  side="Right")
    print("")


print("IN ORDER TRAVERSAL")
inOrderTraversal(mybt)


# PostOrder Traversal of Binary Tree
# Again, actual graph traversal order is identical to previous functions, difference is in where we return the values
# TC: O(n)
# SC: O(n)
def postOrderTraversal(rootNode,node_returns=[], side=None):
    if not rootNode:
        print("     " + (" -> ".join(node_returns)))
        return
    node_returns.append(rootNode.data)
    postOrderTraversal(rootNode.leftChild, node_returns, side="Left")
    postOrderTraversal(rootNode.rightChild, node_returns,  side="Right")
    if side == 'Left':
        print("L: ", rootNode.data)
    elif side == 'Right':
        print("R:", rootNode.data)
    else:
        print("-:", rootNode.data)
    print("")


print("POST ORDER TRAVERSAL")
postOrderTraversal(mybt)


#LevelOrder Traversal of Binary Tree

def levelOrderTraversal(rootNode,node_returns=[], side=None):
    if not rootNode.leftChild and not rootNode.rightChild:
        return
    node_returns.append(rootNode.data)
    if side == 'Left':
        print("L: ", rootNode.data)
    elif side == 'Right':
        print("R:", rootNode.data)
    else:
        print("-:", rootNode.data)
    print("")
    levelOrderTraversal(rootNode.leftChild, node_returns, side="Left")
    levelOrderTraversal(rootNode.rightChild, node_returns,  side="Right")


print("LEVEL ORDER TRAVERSAL")
levelOrderTraversal(mybt)