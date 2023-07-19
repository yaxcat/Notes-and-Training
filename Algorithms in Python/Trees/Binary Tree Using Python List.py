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

    # TC: O(n)
    # SC: O(n)
    def preOrderTraversal(self, index, traversal_result=[], side="-"):
        # If the index supplied is bigger than the tree size, just return
        if index > self.lastUsedIndex:
            print("     Side: " + side + " Index: " + str(index) + " " + "Exit condition reached")
            return 
        print("Side:", side, "Index:", index, "Node:", self.list[index])
        traversal_result.append(self.list[index])
        # Recursively call the function to visit the left & right side of the tree.
        # For why this works, see the diagram: Binary Search Tree with Python List 
        self.preOrderTraversal(index*2, traversal_result, "L") # Visit left side of the tree
        self.preOrderTraversal(index*2 + 1, traversal_result, "R") # Visit the right side of the tree
        return traversal_result
    
    # TC: O(n)
    # SC: O(n)
    def inOrderTraversal(self, index, traversal_result=[], side="-"):
        if index > self.lastUsedIndex:
            print("     Side: " + side + " Index: " + str(index) + " " + "Exit condition reached")
            return
        self.inOrderTraversal(index*2, traversal_result, "L") # Visit left side of the tree
        print("Side:", side, "Index:", index, "Node:", self.list[index])
        traversal_result.append(self.list[index])
        self.inOrderTraversal(index*2 + 1, traversal_result, "R") # Visit the right side of the tree
        return traversal_result
    
    # TC: O(n)
    # SC: O(n)
    def postOrderTraversal(self, index, traversal_result=[], side="-"):
        if index > self.lastUsedIndex:
            print("     Side: " + side + " Index: " + str(index) + " " + "Exit condition reached")
            return
        self.postOrderTraversal(index*2, traversal_result, "L")
        self.postOrderTraversal(index*2+1, traversal_result, "R")
        print("Side:", side, "Index:", index, "Node:", self.list[index])
        traversal_result.append(self.list[index])
        return traversal_result
    
    def levelOrderTraversal(self, index):
        traversal_result = []
        for i in range( index, self.lastUsedIndex+1):
            traversal_result.append(self.list[i])
        return traversal_result
    
    # TC: O(n)
    # SC: O(1)
    def deleteNode(self, value):
        if self.lastUsedIndex == 0:
            return "There are no nodes to delete"
        # Loop over all the nodes in the tree to look for the value we want to change
        for i in range(1, self.lastUsedIndex+1):
            if self.list[i] == value: # If we've found the value we want to delete
                self.list[i] = self.list[self.lastUsedIndex] # Change the value of the node we're deleting to that of the deepest node in the tree
                self.list[self.lastUsedIndex] = None # Delete the deepest node in the tree, since its now in a different place
                self.lastUsedIndex -= 1 # We just deleted a node, so decrement lastUsedIndex
                return "The node has been updated"

    def deleteEntireTree(self):
        self.list = None
    

mybt = BinaryTree(15)
mybt.insertNode("N1")
mybt.insertNode("N2")
mybt.insertNode("N3")
mybt.insertNode("N4")
mybt.insertNode("N5")
mybt.insertNode("N6")
mybt.insertNode("N7")
mybt.insertNode("N8")
mybt.insertNode("N9")

print(mybt.list)

#print("Pre-Order Traversal")

#print("Level Order: ", mybt.levelOrderTraversal(1))
#print("")
print("")
print("Pre Order:   ")
print(mybt.preOrderTraversal(1))
print("")
#print("")
#print("In Order:    ")
#print(mybt.inOrderTraversal(1))
#print("")
#print("")
#print("Post Order:  ")
#print(mybt.postOrderTraversal(1))
#print("")
#print("")

#print("Level Order: ")
#print(mybt.levelOrderTraversal(1))
#print("")

#print(mybt.deleteNode("N4"))

#print("Level Order: ")
#print(mybt.levelOrderTraversal(1))
#print("")