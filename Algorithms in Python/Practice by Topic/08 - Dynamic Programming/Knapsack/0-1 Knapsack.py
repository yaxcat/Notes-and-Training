from functools import lru_cache

# Use top down dynamic programming to solve this combinatorial problem
def knapsack(weights: list[int], values: list[int], max_weight: int) -> int:
    # Pair the weights with the values
    pairs = list(zip(weights, values))
    n = len(pairs)
    
    # Use DFS to explore the state space tree
    @lru_cache(maxsize=None) # Memoize using the dfs fn arguments as a key
    def dfs(curr_ind, capacity):
        # Base case - we've either hit capacity or run out of items
        if capacity == 0 or curr_ind == n:
            return 0

        # Decision to include current item or not is binary and implemented
        # by adding the current list item to the state or not
        skip = dfs(curr_ind+1, capacity)
        take = 0
        # Only recursively explore the path opened by taking the current object
        # if we can fit it in the knapsack to begin with
        if pairs[curr_ind][0] <= capacity:
            # Add the current item and update capacity accordingly
            take += pairs[curr_ind][1] + dfs(curr_ind+1, capacity-pairs[curr_ind][0])
        
        # Bubble the result at the current paths up
        return max(skip, take)
        
    return dfs(0, max_weight)

if __name__ == "__main__":
    weights = [int(x) for x in input().split()]
    values = [int(x) for x in input().split()]
    max_weight = int(input())
    res = knapsack(weights, values, max_weight)
    print(res)
