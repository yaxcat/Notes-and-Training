# Uses bottom up dynamic programming to compute possible weights
def knapsack_weight_only(weights: list[int]) -> list[int]:
    n = len(weights) # Number of individual weight values
    m = sum(weights) # Number of total possible weight values

    # Initialize the DP list.  X axis represents all possible
    # weights from 0 to max_weight. Y axis represents the sequentially
    # increasing combination of list elements from none to all
    dp = [[False for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = True # This state is reachable by putting no items in the bag

    # The idea is to loop over every combination of possible item
    # combinations and weights (states) and determine if it is
    # possible to reach that total weight using a combination of
    # the available items
    for i in range(1, n+1): # Loop over list elements
        for j in range(0, m+1): # Loop over possible total weights
            # For any combination of list values longer than
            # the previous ones tested, we know if it was possible
            # to combine them into the given weight before, it will
            # be possible now
            dp[i][j] = dp[i][j] or dp[i-1][j]
            # Make sure the current sum j is large enough to allow including 
            # the current item's weight
            if j - weights[i-1] >= 0:
                # We check if we can form sum j by including the current item's 
                # weight weights[i-1]. We do this by checking whether sum j - weights[i-1] 
                # was possible using the first i-1 items. If so, then j is now possible
                dp[i][j] = dp[i][j] or dp[i-1][j-weights[i-1]]
    result = []
    # push any valid combination of weights to our results list
    for j in range(0, m+1):
        if dp[n][j]:
            result.append(j)   

    return result

if __name__ == "__main__":
    weights = [int(x) for x in input().split()]
    res = knapsack_weight_only(weights)
    print(" ".join(map(str, sorted(res))))
