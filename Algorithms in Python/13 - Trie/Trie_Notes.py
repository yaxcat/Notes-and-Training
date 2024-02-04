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
            node = current.children.get((letter)) # Attempt to retrieve letter from trie
            # Check to see if the letter is in the Trie
            if node == None:
                node = TrieNode() # If the letter is not there, create a new node to hold it
                current.children.update({letter:node}) # Add the new key:value pair to the dict
            current = node # update current so that we can work our way down the trie
        current.endOfString = True # After everything is done, make sure we're tagging the branch as EOS
        print(f"Successfully inserted {word}")




newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Apple")