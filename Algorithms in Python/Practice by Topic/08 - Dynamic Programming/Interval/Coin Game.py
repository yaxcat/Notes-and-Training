def coin_game(coins: list[int]) -> int:
    n = len(coins)
    
    # Compute prefix sums. Each element will be the total value of
    # all coins up to that point
    prefix_sum = [0 for i in range(n+1)]
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + coins[i-1]
    
    # Initialize the DP table. This will store the result of optimal play
    # (maximum possible score) for a given interval of coins
    dp = [[0 for i in range(n+1)] for j in range(n+1)]

    # Iterate over all valid intervals in the coins list
    for size in range(n): # Size of the coins list
        # Identify left and right boundaries of subarray
        for left in range(1, n-size+1): # Will start at single element interval in top left
            right = left + size
            # Base case, we've got only the one coin
            if left == right:
                dp[left][right] = prefix_sum[right] - prefix_sum[left-1] # Compute the value of the lone coin
            else:
                # The total sum of coins in this interval is given by the prefix sum.
                # We subtract the minimum score the opponent could achieve from the remaining coins,
                # because the opponent will play optimally on their turn.
                dp[left][right] = prefix_sum[right] - prefix_sum[left-1]-min(dp[left+1][right], dp[left][right-1])
    # Return the result of the full game
    return dp[1][n]

if __name__ == "__main__":
    coins = [int(x) for x in input().split()]
    res = coin_game(coins)
    print(res)
