
from functools import lru_cache
from math import inf

# Top down approach, will blow the recursion limit for some test sizes n.
# Should use iterative approach instead.
def perfect_squares(n: int) -> int:
    # Precompute the potential squares for efficiency and ease of
    # scripting; setting the upper bound to the square root of n
    # plus one to account for all useful squares while excluding
    # those that are too large
    squares = [i*i for i in range(1, int(n**0.5)+1)]
    @lru_cache(maxsize=None) # Memoize min squares by curr_ind-capacity key
    # Use DFS to recursively explore the state space
    def dfs(curr_ind, capacity):
        # Base case 1, we cannot fit any more squares so return 0
        if capacity == 0:
            return 0
        # Base case 2, we exceeded the length of potential squares
        # Shouldn't really happen, return infinity
        if curr_ind == len(squares):
            return inf
        skip = dfs(curr_ind+1, capacity)
        # Unbounded knapscack problem, so we can reuse the same curr_indue repeatedly
        add = inf # Ensures that if we add a square that doesn't fit, evaluate correctly
        if squares[curr_ind] <= capacity:
            add = 1 + dfs(curr_ind, capacity-squares[curr_ind]) # Redefine add if we're under capacity
        return min(skip, add) # Bubble the minimum required up during unwinding

    result = int(dfs(0, n))
    return result

if __name__ == "__main__":
    n = int(input())
    res = perfect_squares(n)
    print(res)
