from typing import List


def generate_parentheses(n: int) -> List[str]:
    parentheses = [] # Holds the final list of valid parentheses combinations
    paths = [] ## Tracks the current path of parentheses being constructed (used for backtracking)
    # Explore the state space tree to look for valid parentheses
    def dfs(start, open_count, close_count):
        # Base case: If the path length equals n*2, we've constructed a valid combination
        # of parentheses (n pairs) and can add it to the results.
        if start == n*2:
            parentheses.append("".join(paths)) # Required output is a string
            return
        # If the number of open parentheses is < n, we can continue exploring this
        # branch of the tree because we have enough space left to add an equal number
        # of closing parentheses
        if open_count < n:
            paths.append('(') # Add an open parenthesis to the current path
            dfs(start+1, open_count+1, close_count)
            paths.pop() # Backtrack by removing the last added parenthesis
        # If the number of close parentheses is < the number of open parentheses then
        # we know there is enough space left to potentially balance out the branch with
        # closing parentheses so proceed with exploration
        if close_count < open_count:
            paths.append(')') # Add a closing parenthesis to the current path
            dfs(start+1, open_count, close_count+1)
            paths.pop() # Backtrack by removing the last added parenthesis
    dfs(0, 0, 0)
    return parentheses

if __name__ == "__main__":
    n = 2
    res = generate_parentheses(n)
    for line in sorted(res):
        print(line)
