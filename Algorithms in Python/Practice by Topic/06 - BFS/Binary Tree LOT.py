from typing import List
from collections import deque

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def level_order_traversal(root: Node) -> List[List[int]]:
    if not root:
        return []
    result = []
    q = deque([root]) # Enqueue the root to kick things off
    while len(q) > 0:
        cur_node = q.pop()
        result.append(str(cur_node.val))
        if cur_node.left is not None:
            q.append(cur_node.left)
        if cur_node.right is not None:
            q.append(cur_node.right)
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
    s = '1 2 4 x 7 x x 5 x x 3 x 6 x x'
    root = build_tree(iter(s.split()), int)
    res = level_order_traversal(root)
    for row in res:
        print(" ".join(map(str, row)))
