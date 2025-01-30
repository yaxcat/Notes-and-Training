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
            print(word, "-", combo)
            dfs(start+1)
            combinations.pop()
    res = dfs(0)
        
    return res

if __name__ == "__main__":
    s = "abcd"
    txt = 'a abc b cd'
    words = txt.split()
    res = word_break(s, words)
    print("true" if res else "false")

