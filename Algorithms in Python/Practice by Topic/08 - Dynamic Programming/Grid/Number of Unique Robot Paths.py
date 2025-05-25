# Uses top down dynamic programming to reduce time complexity of finding the
# number of paths which satisfy the problem constraints
def unique_paths(m: int, n: int) -> int:
    memo = {} # Memoize using grid position as key since this determines subsequent paths

    def dfs(r, c):
        # First check to see if we have a memoized result
        if (r, c) in memo:
            return memo[(r, c)]
        # Base case, we have reached the goal position, so return 1 indicating its a valid path
        if r == m-1 and c == n-1:
            return 1
        # Prune branches which have extended beyond the grid domain
        if r > m-1 or c > n-1:
            return 0
        # Recursively explore state space tree of potential paths
        total_paths = 0
        total_paths += dfs(r+1, c)
        total_paths += dfs(r, c+1)
        
        # Add new path to the memo
        memo[(r, c)] = total_paths

        return total_paths

    result = dfs(0, 0)

    return result

if __name__ == "__main__":
    m = int(input())
    n = int(input())
    res = unique_paths(m, n)
    print(res)
