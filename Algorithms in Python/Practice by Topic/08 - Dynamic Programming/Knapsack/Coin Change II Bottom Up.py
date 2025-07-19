# Constraints of the problem indicate that we should use a bottom up approach
# with Python, as there is a chance we might blow the recursion limit otherwise
def coin_game(coins: list[int], amount: int) -> int:
    # Initialize dp list. We only need a 1D list because we can use the same coin
    # more than once and thus don't need to track usage
    dp = [0 for _ in range(amount+1)]
    dp[0] = 1 # One way to make zero

    # Loop over coins first and then start at the current coin value in the second
    # loop. This ensures that we eliminate duplicates (permunations like [1,2] vs [2,1]),
    #  we only add ways after all coins smaller than current coin have been considered.
    for coin in coins:
        for i in range(coin, amount+1):
        # For each amount i ≥ coin, add the number of ways to make (i - coin) to dp[i]
        # This accumulates all combinations that include the current coin
            dp[i] += dp[i-coin]
    return dp[amount]

if __name__ == "__main__":
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_game(coins, amount)
    print(res)
