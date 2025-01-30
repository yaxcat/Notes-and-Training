from typing import List

def permutations(letters: str) -> List[str]:
    result = [] # Stores permutations
    path = []  # Tracks the current permutation being constructed
    used = [False] * len(letters) # Marks whether a letter has been used in the current branch
    # Helper function to perform DFS and generate permutations
    def dfs(start):
        # Base case: If the path length equals the input string length,
        # we have constructed a complete permutation.
        if start == len(letters):
            result.append(''.join(path)) # Add the current permutation to the result list
            return
        # Loop through the entire input string
        for i, letter in enumerate(letters):
            # Skip this letter if it has already been used in the current branch
            if used[i] == True:
                continue
            # Add the letter to the current path and mark it as used
            path.append(letter)
            used[i] = True
            dfs(start+1) # Recursively explore further permutations with the updated path
            # Backtrack: Remove the letter from the path and mark it as unused
            path.pop() 
            used[i] = False
    dfs(0)
    return result

if __name__ == "__main__":
    letters = 'abc'
    res = permutations(letters)
    for line in sorted(res):
        print(line)
