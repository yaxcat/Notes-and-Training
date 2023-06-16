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

print(tree)



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
    
new_bt = TreeNode("Drinks")
