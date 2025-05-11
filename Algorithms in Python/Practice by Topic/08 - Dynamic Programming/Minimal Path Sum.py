from math import inf

# Top down approach - Recursively explore potential paths, prune exploration
# of those that track out of bounds and bubble the minimal cost path up to
# answer the question. Use memoization to reduce time complexity
def min_path_sum(grid: list[list[int]]) -> int:
    # Get grid dimensions
    num_rows = len(grid)
    num_cols = len(grid[0])

    # Key is coordinate position, since this determines subsequent path nav
    # decisions. Value is minimum cost path so far
    memo = {}

    # Use DFS to recursively explore the state space and find navicable
    # paths from the starting position to the goal and then evaluate their
    # costs
    def dfs(r, c):
        # Check the memo first
        if (r, c) in memo:
            return memo[(r, c)]

        # Base case, we've reached the goal position
        if r == num_rows-1 and c == num_cols-1:
            return grid[r][c]
        
        # Prune away branches that exceed the grid domain
        if r > num_rows-1 or c > num_cols-1:
            return inf
        
        # Recursively explore potential paths, we must explore all paths first
        # and then bubble the minimum-so-far value up as recursion unwinds. This
        # corresponds to navigating the grid in reverse from the goal position to
        # the start
        
        min_path =  grid[r][c] + min(dfs(r+1, c), dfs(r, c+1))
        memo[(r,c)] = min_path

        return min_path
        
    result = dfs(0,0)

    return result

if __name__ == "__main__":
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = min_path_sum(grid)
    print(res)
