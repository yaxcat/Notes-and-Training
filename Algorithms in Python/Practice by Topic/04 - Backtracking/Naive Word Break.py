from typing import List

# Identify whether or not a list of words can be combined to match the target word
def word_break(s: str, words: List[str]) -> bool:
    # Holds the combinations of individual input words as we explore the state space tree
    combinations = []
    memo = {}
    # Traverses the SST using depth first search
    def dfs(start):
        # Base case - we've reached the end of the words list without finding a match on this
        # branch, so return false
        if start == len(words):
            return False
        # Loop through the individual words in the list and test combinations of those words
        # to determine if they match the target
        for word in words:
            combo = ''.join(combinations) + word
            combinations.append(word)
            result = s == combo

            if start in memo:
                return memo[start]

            # Test to see if a match has been found before beginning the recursion so that
            # we can bubble the result up
            if result == True:
                return True
            # If we have not found a match, continue exploring the tree. Pop the combinations
            # list to keep it synced with the words list
            else:
                memo[start] = dfs(start+1)
                combinations.pop()
    res = dfs(0)
        
    return res

if __name__ == "__main__":
    s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
    txt = 'a aa aaa aaaa aaaaa aaaaaa aaaaaaa aaaaaaaa aaaaaaaaa aaaaaaaaaa'
    words = txt.split()
    res = word_break(s, words)
    print("true" if res else "false")

