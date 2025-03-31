from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_min_depth(root: Node) -> int:
    if root is None:
        return 0
    q = deque([root])
    level = 0
    while len(q) > 0:
        num_nodes = len(q)
        for _ in range(num_nodes):
            curr_node = q.popleft()
            if curr_node.left is None and curr_node.right is None:
                return level
            if curr_node.left is not None:
                q.append(curr_node.left)
            if curr_node.right is not None:
                q.append(curr_node.right)
        level += 1
    return level

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
    s = '1 2 4 x 7 x x 5 x x 3 x 6 x x'
    root = build_tree(iter(s.split()), int)
    res = binary_tree_min_depth(root)
    print(res)
