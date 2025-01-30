from math import inf
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def visible_tree_node(root: Node) -> int:
    # Use preorder traversal so that we can examine the height of each node
    # along the path as we descend the from the root to the leaf
    def preorder_traversal(root, max_so_far):
        # Base case, we've hit the bottom of the tree
        if root is None: 
            return 0
        # Create a variable total, to hold the number of visible nodes we've
        # encountered so far
        total = 0
        # If the current node is greater than the max value we've encountered
        # on the path, its visible
        if root.val >= max_so_far:
            total += 1
        # Recursively traverse the tree, increasing total as we find visible
        # nodes
        total += preorder_traversal(root.left, max(root.val, max_so_far))
        total += preorder_traversal(root.right, max(root.val, max_so_far))

        return total

    return preorder_traversal(root, -inf) # Root will register since its bigger than -inf

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
    res = visible_tree_node(root)
    print(res)
