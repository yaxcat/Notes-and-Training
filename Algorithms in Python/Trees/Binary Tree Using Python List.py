# BINARY SEARCH TREE USING PYTHON LIST
# TC: O(1)
# SC: O(n) due to creation of list
class BinaryTree:
    def __init__(self, size):
        self.list = size * [None] # Initialize the list to a set size to improve performance
        self.lastUsedIndex = 0 # We never actually use 0 in this scheme, so using as a default is fine
        self.maxSize = size

    # Inserts a node at the next available spot
    # TC: O(1)
    # SC: O(1)
    def insertNode(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        # Note that to add a value to the tree, we're simply using the last used index. This means that the 
        # parent-child relationship is actually created post-hoc, rather than being baked in from the beginning
        # as with the linked list implementation.
        self.list[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return f"The value: {value} has been successfully inserted at position: {self.lastUsedIndex}"
    
    # Searches a binary tree for a given value:
    # TC: O(n)
    # SC: O(n)
    def levelOrderTraversalSearch(self, target):
        # LOT search implementation is considerably simpler than if using a linked list
        for i in range(1, self.lastUsedIndex+1):
            if self.list[i] == target:
                return self.list[i]
        return "Target value not found"


    def preOrderTraversal(self):
        

mybt = BinaryTree(15)
print(mybt.insertNode("N1"))
print(mybt.insertNode("N2"))
print(mybt.insertNode("N3"))
print(mybt.insertNode("N4"))
print(mybt.insertNode("N5"))
print(mybt.insertNode("N6"))
print(mybt.insertNode("N7"))
print(mybt.insertNode("N8"))
print(mybt.insertNode("N9"))

print(mybt.list)

print(mybt.levelOrderTraversalSearch("N90"))