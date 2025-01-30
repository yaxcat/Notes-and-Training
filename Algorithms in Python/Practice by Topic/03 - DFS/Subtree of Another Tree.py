class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Helper function to evaluate if the current root is identical to a given subtree
def preorder_traversal(root, sub_root):
    # If both are null, the nodes are identical
    if root is None and sub_root is None:
        return True
    # If one node is null and the other isn't, they are not identical
    if root is None or sub_root is None:
        return False
    # Recursively traverse the tree and subtree to see if they are identical
    return (
            root.val == sub_root.val and 
            preorder_traversal(root.left, sub_root.left) and 
            preorder_traversal(root.right, sub_root.right)
            )
# Controlling function which will traverse the main tree and call the helper function at
# node to check if the main tree's subtree is identical to a given subtree
def subtree_of_another_tree(root: Node, sub_root: Node) -> bool:
    # We have traversed a branch of the main tree without finding an identical subtree
    if root is None:
        return False
    # An identical subtree could be located in the current tree, or its right or left subtrees
    return (
        preorder_traversal(root, sub_root) or # Recusively evaluate from the current position in the main tree
        subtree_of_another_tree(root.left, sub_root) or # Recursively evaluate the left subtree of the main tree
        subtree_of_another_tree(root.right, sub_root) # Recursively evaluate the right subtree of the main tree
        )

# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    if val == "x":
        return None
    left = build_tree(nodes, f)
    right = build_tree(nodes, f)
    return Node(f(val), left, right)

if __name__ == "__main__":
    root = build_tree(iter(input().split()), int)
    sub_root = build_tree(iter(input().split()), int)
    res = subtree_of_another_tree(root, sub_root)
    print("true" if res else "false")
