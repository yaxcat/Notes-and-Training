import math

class BSTNode:
    def __init__(self, data=None, left = None, right= None):
        self.data = data
        self.left = left
        self.right = right

# The key insight to this algorithm is recognizing that the input list will be sorted before we start.
# This means that creating a balanced BST is relatively easy.  The value in the middle of the list will
# be our root node while the value in the middle of the left sublist will be the root's left child,
# while the value in right sublist will be the root's right child.  This will be recursively true through
# the entire list.
def minimalTree(sortedArray):
    arr_len = len(sortedArray)
    mid = arr_len//2 # We only want an integer value
    if arr_len == 0: #Base case
        return None
    # If we've sliced the list all the way down to a single element, we've found a leaf node
    if arr_len == 1: 
        return BSTNode(sortedArray[0]) # We know there is only one element in the array, hence the 0 ind
    # Run the function recursively on the left right half of the list which will keep cutting the lists
    # in half and eventually return a single node for each each half
    left  = minimalTree(sortedArray[:mid])
    right = minimalTree(sortedArray[mid+1:])
    # Finally, create the parent node, setting its child references to the nodes created prior
    return BSTNode(sortedArray[mid], left, right)
    


sortedArray = [1,2,3,4,5,6,7,8,9]

bst = minimalTree(sortedArray)
