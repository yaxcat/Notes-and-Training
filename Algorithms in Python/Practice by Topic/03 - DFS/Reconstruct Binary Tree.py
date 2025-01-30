from typing import List

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# prorder - CLR - [3,9,20,15,7]
# inorder - LCR - [9,3,15,20,7]

# Parses the input lists and uses post order traversal to build a binary tree
def build_tree(preorder_ind, inorder_start, size, value_to_inorder_ind):
    # For reference in debugger.  Serve no purpose other than helping understand
    # what is happening when viewing the call stack
    db_1_preorder_ind = preorder_ind
    db_2_inorder_start = inorder_start
    db_3_size = size
    
    # Base case
    # If the size window of the inorder list we can consider building nodes for
    # is less than 0, we have reached the end of a branch and should return None
    if size < 0:
        return None
    # Define parameters to identify the node value and control the recursion
    root = preorder[preorder_ind] # Identify the root's value from the preorder list
    root_inorder_ind = value_to_inorder_ind[root] # Identify the root's position in the inorder list    
    left_subtree_size = root_inorder_ind - inorder_start # The size of the left subtree can be found by identifying the root's position in the inorder list and then finding the amount of space between it and the inorder starting position to its left?""
    print(root)
    print("---", root_inorder_ind)
    print("------", left_subtree_size)
    # Recursively build the left and right children
    left_child = build_tree(
        preorder_ind+1,
        inorder_start,
        left_subtree_size,
        value_to_inorder_ind
    )
    right_child = build_tree(
        preorder_ind+left_subtree_size+1,
        root_inorder_ind+1,
        size-1-left_subtree_size,
        value_to_inorder_ind
    )
    # Return the constructed node
    return Node(root, left_child, right_child)

def construct_binary_tree(preorder: List[int], inorder: List[int]) -> Node:
    value_to_inorder_ind = {val: idx for idx, val in enumerate(inorder)}
    return build_tree(0, 0, len(preorder), value_to_inorder_ind)

def format_tree(node):
    if node is None:
        yield "x"
        return
    yield str(node.val)
    yield from format_tree(node.left)
    yield from format_tree(node.right)

if __name__ == "__main__":

    po = '3 9 20 15 7'
    io = '9 3 15 20 7'

    preorder = [int(x) for x in po.split()]
    inorder = [int(x) for x in io.split()]
    res = construct_binary_tree(preorder, inorder)
    print(" ".join(format_tree(res)))
