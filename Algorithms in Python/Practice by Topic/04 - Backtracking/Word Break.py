from typing import List

def word_break(s: str, words: List[str]) -> bool:
    # Results cache for memoization
    memo = {}
    # Recursively explores the state space, starting at the beginning of the word
    # and working towards the end of the word as the function traverses down the
    # tree
    def dfs(start, target):
        # Base case, if we've reached the end of a branch, we've found a series of
        # prefixes that form the target word
        if start == len(target):
            return True
        # If we've already explored this branch, return the result we computed the
        # first time and exit to avoid reprocessing duplicate scenarios
        if start in memo:
            return memo[start] 
        # Initialize result variable
        result = False
        # Loop through the word list to explore the state space. The target word
        # is analyzed section by section from left to right, with each section
        # size corresponding to the size of the previously matched substring from
        # the words lis
        for word in words:
            # If the currently unmatched part of the target word starts with a
            # a substring from the words list, return the result if we have reached
            # a leaf node or continue breaking down the target word recursively if
            # we have not
            if target[start:].startswith(word):
                if dfs(start+len(word), target):
                    result = True
        # Cache the result as False if no valid segmentation is found
        memo[start] = result
        return result
    
    return dfs(0, s)

if __name__ == "__main__":
    s = 'algomonster'
    words = ['algo', 'monster']
    res = word_break(s, words)
    print("true" if res else "false")
