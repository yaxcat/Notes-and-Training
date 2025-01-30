from typing import List

def letter_combination(n: int) -> List[str]:
    paths = [] # keeps track of all the combinations returned by the dfs fn
    # Helper function to perform the combinatorial search
    def dfs(start, path):
        elems = ['a', 'b'] # Elements that will be combined to generate letter combinations
        # Base case: When the current recursion depth (start) equals n, the path represents a complete combination, which is added to paths
        if start == n:
            paths.append(''.join(path)) # Join the path list into a string and append it to paths. This avoids appending a mutable reference to the same list, which would lead to all entries being overwritten later.
            return
        # Loop through the elements and recursively build the paths
        for e in elems:
            path.append(e)
            dfs(start+1, path)
            path.pop() # Remove the last element to backtrack and explore other combinations
    dfs(0, [])
    return paths

if __name__ == "__main__":
    n = int(input())
    res = letter_combination(n)
    for line in sorted(res):
        print(line)
