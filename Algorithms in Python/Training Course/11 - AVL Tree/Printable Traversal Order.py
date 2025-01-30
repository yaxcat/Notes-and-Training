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
