# Uses top down dynamic programming to compute the unique sums that can be
# created using the input weights
def knapsack_weight_only(weights: list[int]) -> list[int]:
    n = len(weights)
    unique_sums = set()
    total_sum = sum(weights)
    # It is not enough to memoize by the index value of the weights list
    # alone because this does not uniquely identify the branch. We must 
    # also incorporate the weight at that particular node
    memo = [[False] * (total_sum + 1) for _ in range(n+1)]

    def dfs(start, total):
        # Base case - we have reached the end of the input weights list
        if start == n:
            unique_sums.add(total)
            return
        #We check the memo first to avoid recomputing the same (start, total) 
        # state. We set the memo after exploring both choices, regardless of whether 
        # it's a leaf node.
        if memo[start][total]:
            return
        
        # Reursively explore the unique combinations that can be created
        dfs(start+1, total) # Skips the first item
        dfs(start+1, total+weights[start])
        memo[start][total] = True

    dfs(0, 0)
    return list(unique_sums)

if __name__ == "__main__":
    weights = [int(x) for x in input().split()]
    res = knapsack_weight_only(weights)
    print(" ".join(map(str, sorted(res))))
