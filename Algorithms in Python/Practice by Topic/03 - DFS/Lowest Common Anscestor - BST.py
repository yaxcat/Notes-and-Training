class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Traverse the tree in a top down manner, guiding the search direction based
# on the values of p & q. Does not need to visit every node and as such does
# get bucketed as preorder traversal, inorder traversal, etc. 
def lca_on_bst(bst: Node, p: int, q: int) -> int:
    # Base case
    if bst is None:
        return 0
    # if both p and q are on the left side of the tree, traverse this side
    if p < bst.val and q < bst.val:
        return lca_on_bst(bst.left, p, q)
    # if both p and q are on the right side of the tree, traverse that side
    elif p > bst.val and q > bst.val:
        return lca_on_bst(bst.right, p, q)
    # if p and q are on separate sides of the tree, we have found the LCA, so 
    # return its value
    else:
        return bst.val

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
    bst = build_tree(iter(input().split()), int)
    p = int(input())
    q = int(input())
    res = lca_on_bst(bst, p, q)
    print(res)
