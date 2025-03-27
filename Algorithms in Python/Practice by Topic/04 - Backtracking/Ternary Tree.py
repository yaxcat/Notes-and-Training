from typing import List

class Node:
    def __init__(self, val, children=None):
        if children is None:
            children = []
        self.val = val
        self.children = children

def ternary_tree_paths(root: Node) -> List[str]:
    results = []
    path = []
    def dfs(root):
        # Base case, if the current node has no children,
        # it is a leaf node, so append the path to the results
        # and return
        if all(child is None for child in root.children):
            results.append('->'.join(path) + '->' + str(root.val))
            return
        # Loop through the children and recursively explore the 
        # rest of the tree
        for child in root.children:
            path.append(str(root.val))
            dfs(child)
            path.pop() # After recursion is finished, pop the last element to backtrack to the previous node
    dfs(root)
    return results


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
