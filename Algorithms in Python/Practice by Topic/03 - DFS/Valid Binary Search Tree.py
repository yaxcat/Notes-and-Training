class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def valid_bst(root: Node) -> bool:
    def in_order_traversal(root, arr):
        if not root:
            return None
        in_order_traversal(root.left, arr)
        arr.append(root.val)
        in_order_traversal(root.right, arr)
        return arr

    iot = in_order_traversal(root, [])
    result = True
    if iot is None:
        return result
    else:
        for i in range(0, len(iot)-1):
            if iot[i] > iot[i+1]:
                result = False
    return result

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
    res = valid_bst(root)
    print("true" if res else "false")
