from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> List[str]:
    # Navigate the tree in preorder traversal.  We pass both the current path and results lists in
    # as states so that we can build up a complete description of the tree as we go
    def preorder(root, path, res):
        # Base case, we have reached the end of a branch
        if all(child is None for child in root.children): # If all the children of the current node are null, we have reached the end of a branch
            res.append('->'.join(path) + '->' + str(root.val))  # Construct path string and add it to results.
            return
        # Recursive case: Traverse each non-None child and continue building the path
        for child in root.children:
            if child is not None:
                preorder(child, path + [str(root.val)], res) # Pass the updated path to the recursive call.
    res = [] # Define in the parent fn scope since preorder will append to it as it recurses the tree
    if root: preorder(root, [], res) # Start traversal if the root is not None.
    return res
# this function builds a tree from input; you don't have to modify it
# learn more about how trees are encoded in https://algo.monster/problems/serializing_tree
def build_tree(nodes, f):
    val = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(val), children)

if __name__ == "__main__":
    root = build_tree(iter(input().split()), int)
    res = ternary_tree_paths(root)
    for line in res:
        print(line)
d