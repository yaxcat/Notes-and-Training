class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(tree: Node) -> bool:
    def post_order_traversal(tree):
        # Base case, if there is no node, return 0
        if not tree:
            return 0
        # Calculate the left and right subtree heights first (post order traversal)
        lh = post_order_traversal(tree.left)
        rh = post_order_traversal(tree.right)
        
        # If there is a disblance found in the right or left subtree, simply
        # return that finding and exit
        if lh == -1 or rh == -1:
            return -1
        # Evaluate the balance
        if abs(lh-rh) > 1:
            return -1
        # The return value will be the greater of the left or right heights
        # plus one for the additional node
        return (max(lh, rh)+1)

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
    tree = build_tree(iter(input().split()), int)
    res = is_balanced(tree)
    print("true" if res else "false")
