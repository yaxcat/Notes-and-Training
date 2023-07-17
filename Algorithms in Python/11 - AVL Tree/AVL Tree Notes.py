# AVL TREE

# An AVL tree is a self-balancing binary search tree, where the difference between left and right subtree
# heights cannot be more than one for all nodes.

# Any time the height of the left and right subrees differ by more than one, rebalancing will occur, and this
# process is called 'rotation'

# Utility:
#   Unbalanced binary search trees can get really long on either the right or left subtree.  If the number
#   of nodes is heavily biased to one side or the other, we lose much of the benefit of binary tree for most
#   operations.  The more 'linear' a tree starts to look, the more operational time compexity will tend towards
#   O(n), instead of O(logN).  Performance of a binary tree is tied to the height of the tree.


class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

def preOrderTraversal(rootNode, tr=[]):
    if not rootNode:
        return 
    tr.append(str(rootNode.data))
    preOrderTraversal(rootNode.leftChild, tr)
    preOrderTraversal(rootNode.rightChild, tr)
    return tr

def inOrderTraversal(rootNode, tr=[]):
    if not rootNode:
        return 
    inOrderTraversal(rootNode.leftChild, tr)
    tr.append(str(rootNode.data))
    inOrderTraversal(rootNode.rightChild, tr)
    return tr

def postOrderTraversal(rootNode, tr=[]):
    if not rootNode:
        return 
    postOrderTraversal(rootNode.leftChild, tr)
    postOrderTraversal(rootNode.rightChild, tr)
    tr.append(str(rootNode.data))
    return tr

import QueueHelper as qh
def levelOrderTraversal(rootNode):
    traversal_result = []
    q = qh.Queue()
    q.enqueue(rootNode)
    while q.isEmpty() is False:
        root = q.dequeue()
        traversal_result.append(root.value.data)
        if root.value.leftChild is not None:
            q.enqueue(root.value.leftChild)
        if root.value.rightChild is not None:
            q.enqueue(root.value.rightChild)
    return traversal_result


def printablePreOrderTraversal(rootNode, tr=[], depth=0):
    if not rootNode:
        return
    indent = " " * depth * 4
    print(f"{indent}└── APPEND: {str(rootNode.data)})")
    tr.append(str(rootNode.data))
    if not rootNode.leftChild:
        print_lc = 'None'
    else:
        print_lc = str(rootNode.leftChild.data)
    if not rootNode.rightChild:
        print_rc = 'None'
    else:
        print_rc = str(rootNode.rightChild.data)
    
    print(f"{indent}preOrderTraversal(rootNode={rootNode.data})")
    print(f"{indent}│")
    print(f"{indent}├── LEFT: preOrderTraversal({print_lc})")
    printablePreOrderTraversal(rootNode.leftChild, tr, depth + 1)
    print(f"{indent}└── RIGHT: preOrderTraversal({print_rc})")
    printablePreOrderTraversal(rootNode.rightChild, tr, depth + 1)
    return tr

def printableInOrderTraversal(rootNode, tr=[], depth=0):
    if not rootNode:
        return
    if not rootNode.leftChild:
        print_lc = 'None'
    else:
        print_lc = str(rootNode.leftChild.data)
    if not rootNode.rightChild:
        print_rc = 'None'
    else:
        print_rc = str(rootNode.rightChild.data)
    indent = " " * depth * 4
    print(f"{indent}inOrderTraversal(rootNode={rootNode.data})")
    print(f"{indent}│")
    print(f"{indent}├── LEFT: inOrderTraversal({print_lc})")
    printableInOrderTraversal(rootNode.leftChild, tr, depth+1)
    print(f"{indent}└── APPEND: {str(rootNode.data)})")
    tr.append(str(rootNode.data))
    print(f"{indent}└── RIGHT: inOrderTraversal({print_rc})")
    printableInOrderTraversal(rootNode.rightChild, tr, depth+1)
    return tr


def printablePostOrderTraversal(rootNode, tr=[], depth=0):
    if not rootNode:
        return 
    
    if not rootNode.leftChild:
        print_lc = 'None'
    else:
        print_lc = str(rootNode.leftChild.data)
    if not rootNode.rightChild:
        print_rc = 'None'
    else:
        print_rc = str(rootNode.rightChild.data)
    indent = " " * depth * 4
    print(f"{indent}postOrderTraversal(rootNode={rootNode.data})")
    print(f"{indent}│")
    print(f"{indent}├── LEFT: postOrderTraversal({print_lc})")
    printablePostOrderTraversal(rootNode.leftChild, tr, depth+1)
    print(f"{indent}└── RIGHT: postOrderTraversal({print_rc})")
    printablePostOrderTraversal(rootNode.rightChild, tr, depth+1)
    print(f"{indent}└── APPEND: {str(rootNode.data)})")
    tr.append(str(rootNode.data))
    return tr

# TC: O(logN) since we're halving the search area each time
def searchNode(rootNode, searchVal):
    if rootNode.data == searchVal:
        return "Node found at root: " + searchVal
    else:
        if searchVal < rootNode.data:
            if rootNode.leftChild.data == searchVal:
                return "Node found on left: " + searchVal
            else:
                searchNode(rootNode.leftChild, searchVal)
        else:
            if rootNode.rightChild == searchVal:
                return "Node found on right: " + searchVal
            else:
                searchNode(rootNode.rightChild, searchVal)



# For AVL tree node insertion, one of two scenarios will be true:
#   1. Rotation (balancing) is not required
#   2. Rotation (balancing) is required
#       a.  left left condition (LL)        
#       b.  left right condition (LR)
#       c.  right right condition (RR)
#       d.  right left condition (RL)
def insertNode(rootNode, newVal):
    if not rootNode:
        return "The tree does not exist"
    if newVal < rootNode.data:
        if not rootNode.leftChild:
            rootNode.leftChild = AVLNode(newVal)
        else:
            insertNode(rootNode.leftChild, newVal)
    else:
        if not rootNode.rightChild:
            rootNode.rightChild = AVLNode(newVal)
        else:
            insertNode(rootNode.rightChild, newVal)


mybt = AVLNode(70)

insertNode(mybt, 50)
insertNode(mybt, 90)
insertNode(mybt, 30)
insertNode(mybt, 60)
insertNode(mybt, 80)
insertNode(mybt, 100)
insertNode(mybt, 20)
insertNode(mybt, 40)
insertNode(mybt, 95)
insertNode(mybt, 105)

print("PRE ORDER TRAVERSAL")
print(printablePreOrderTraversal(mybt))
print("\n"*2)
print("IN ORDER TRAVERSAL")
print(printableInOrderTraversal(mybt))
print("\n"*2)
print("POST ORDER TRAVERSAL")
print(printablePostOrderTraversal(mybt))
print("\n"*2)
#print(levelOrderTraversal(mybt))


#print(mybt.rightChild.rightChild.data)