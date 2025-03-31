from typing import List
from collections import deque
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_right_side_view(root: Node) -> List[int]:
    if not root:
        return []
    result = []
    q = deque([root])
    while len(q) > 0:
        num_nodes = len(q)
        for i in range(num_nodes):
            cur_node = q.popleft()
            if i == num_nodes-1:
                result.append(cur_node.val)
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
    res = binary_tree_right_side_view(root)
    print(" ".join(map(str, res)))
