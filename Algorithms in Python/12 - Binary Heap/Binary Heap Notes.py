# BINARY HEAP

# A binary heap is a binary tree with additional properties:
#   1. A binary heap will be either a min heap or a max heap
#       - Min Heap - the root value must be equal to or smaller than all the values of its children and this must be recursively true for all nodes in the tree
#       - Max Heap - the root value must be equal to or larger than all the values of its children and this must be recursively true for all nodes in the tree
#   2.  It is complete - all levels are completely filled except possibly the last level, which if not filled, has all keys as left as possible.  This
#       property makes binary heaps suitable for storing in arrays
#
#   * Binary heaps are not guaranteed to balanced in the way that AVL trees are.
#     While AVL trees are used to efficiently search for, insert or delete elements, binary heaps are primarily used to extract the min or max element of a
#     collection in constant time, which is better than O(logN) as with AVL trees.  They are commonly used with priority queues.
#
#
#   Best implemented via array


# Creating the heap
# TC: O(1)
# SC: O(1) - because we're creating a new Python list with n elements
class Heap:
    def __init__(self, size):
        self.customList = (size+1) * [None] # create an empty list equal to the size paramter plus one
        self.heapSize = 0
        self.maxSize = size +1 # We add one because we do not use the first slot (index 0) in order to make the calculations easier

# Peek simply returns the root node
def peek(rootNode):
    if not rootNode:
        return "There is no root to peek at"
    else:
        return rootNode.customList[1] # The root will always be at index 1 in a Python list
    
# Since the size property is defined in the class, all we need to do is access the object property
def getHeapSize(rootNode):
    if not rootNode:
        return "The heap is empty"
    else:
        return rootNode.heapSize

# LOT is easy since we're using a list to store the data
def levelOrderTraversal(rootNode):
    if not rootNode:
        return "The heap is empty"
    else:
        for i in range(1, rootNode.heapSize+1): # Start at 1 because the 0 slot is always left empty
            print(rootNode.customList[i])

mybh = Heap(10)

# Maintains the heap structure of the data
def heapifyTreeInsert(rootNode, index, heapType):
    parentIndex = int(index/2)
    if index <= 1:
        return "Reached the top of the heap"
    if heapType == "Min":
        # In a minimum heap, the root node must always be less than its children, so if the child we
        # just inserted is less than its parent, we have a problem
        if rootNode.customList[index] < rootNode.customList[parentIndex]:    
            temp = rootNode.customList[index] # Create a temporary node equal to the node we just inserted
            rootNode.customList[index] = rootNode.customList[parentIndex] # Because the new node is less than its parent, move the parent to the location of the new node
            rootNode.customList[parentIndex] = temp # Now, change set the parent node slot as equal to the new node, since its smaller than the original parent
        heapifyTreeInsert(rootNode, parentIndex, heapType) # Recursively call the function so that we can walk all the way up the tree if we need to