
# Uses top down dynamic programming to identify the least costly path to 
# the bottom of the triangle
def minimum_total(triangle: list[list[int]]) -> int:
    # Memoize path costs by position to reduce time complexity
    memo = {}
    num_rows = len(triangle)
    # Use DFS to identify all viable paths and bubble the minimum up during
    # recursion unwinding
    def dfs(r, c):
        # If path segment has been traversed before, we already know the
        # minimum value, so just return it
        if (r, c) in memo:
            return memo[(r, c)]
        
        # Base case, we have hit the bottom of the triangle
        if r == num_rows-1:
            return triangle[r][c]
        
        # Recurse over the triangle and evaluate the paths
        min_path = min(
            dfs(r+1, c),
            dfs(r+1, c+1)
        )
        # Memoize, make sure to include the current location to build the
        # path correctly
        memo[(r, c)] = triangle[r][c] + min_path
        # Bubble minimum path so far from the bottom up during unwinding
        return memo[(r, c)]
    return dfs(0, 0)

if __name__ == "__main__":
    triangle = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = minimum_total(triangle)
    print(res)
