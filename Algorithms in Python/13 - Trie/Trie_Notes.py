# Trie is a tree data structure that organizes information in a heirarchical fashion.  It is used
# with strings, unlike other trees.  In a trie, a character or characters are stored at each node, 
# which enables fast finding of words stored in the tree.

# Some uses include autocomplete and spell checking

# PROPERTIES
# 1) Typically used to store strings - space and time efficient
# 2) Any node in trie an store non-repetive characters and each node can store multiple characters.
# 3) Every node stores a link to the next character in the string
# 4) Every node keeps track of where the 'end of string' is.

# OPERATIONS
# 1) Creation of trie
# 2) Insertion in trie
# 3) Searching for string in trie
# 4) Deletion from trie


class TrieNode:
    def __init__(self): # All nodes are blank (no value) at first
        self.children = {} # A dictionary is a very useful way to keep track of child nodes
        self.endOfString = False 


class Trie:
    def __init__(self):
        self.rootNode = TrieNode() # All we need to do here is initialize a blank root node


    def insertString(self, word):
        current = self.rootNode
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print("Successfully inserted")
    

    """
    # Inserting a string - 
        # A few scenarios - 
            # 1) Trie is blank
            # 2) New string shares a prefix with an existing string
            # 3  New string's prefix is already present as a complete string
            # 4) String to be inserted is already present in trie  
    # TC: O(m) - Length of the word we want to insert
    # SC: O(m) - Length of the word we want to insert
    def insertString(self, word):
        current = self.rootNode
        for letter in word:
            node = current.children.get(letter) # Attempt to retrieve letter from trie
            # Check to see if the letter is in the Trie
            if node == None:
                node = TrieNode() # If the letter is not there, create a new node to hold it
                current.children.update({letter:node}) # Add the new key:value pair to the dict
            current = node # update current so that we can work our way down the trie
        current.endOfString = True # After everything is done, make sure we're tagging the branch as EOS
        print(f"Successfully inserted {word}")
    """

    # Searching for a string:
        # Scenarios - 
            # 1) String does not exist in Trie
            # 2) String does exist
            #    - EOS must read true
            # 3) String is a prefix of another string in Trie, but does not exist in Trie
            #    -EOS for the prefix will read false/not exist
    # TC: O(m) 
    # SC: O(1)
    def searchString(self, word):
        currentNode = self.rootNode
        for letter in word:
            node = currentNode.children.get(letter)
            if node == None:
                print("---Node is none")
                return False # Scenario 1
            currentNode = node    

            nodeChildren = [", ".join(key) for key in node.children]
            print(nodeChildren, "||", node.endOfString)

            if currentNode.endOfString == True:
                print("---Node found!")
                return True # Scenario 2
            else:
                print("---Node does not have EOS == True")
                return False # Scenario 3
        print("\n\n\n")


newTrie = Trie()
newTrie.insertString("App")
print("\n\n")
#newTrie.insertString("Apple")
#newTrie.searchString("App")
#print(newTrie.rootNode["A"])

print(newTrie.rootNode.children, "||", newTrie.rootNode.endOfString)
print("A", newTrie.rootNode.children["A"], "||", newTrie.rootNode.children["A"].endOfString)
print("p", newTrie.rootNode.children["A"].children["p"], "||", newTrie.rootNode.children["A"].children["p"].endOfString)
print("p", newTrie.rootNode.children["A"].children["p"].children["p"], "||", newTrie.rootNode.children["A"].children["p"].children["p"].endOfString)

print("\n\n\n")