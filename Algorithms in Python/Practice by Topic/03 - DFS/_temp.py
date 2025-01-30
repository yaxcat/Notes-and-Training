class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca_on_bst(bst: Node, p: int, q: int) -> int:
    if not bst:
        return None
    if p < bst.val and q < bst.val:
        return lca_on_bst(bst.left, p, q)
    elif p > bst.val and q > bst.val:
        return lca_on_bst(bst.right, p, q)
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
    bst = build_tree(iter('6 2 0 x x 4 3 x x 5 x x 8 7 x x 9 x x'.split()), int)
    p = 2
    q = 8
    res = lca_on_bst(bst, p, q)
    print(res)
