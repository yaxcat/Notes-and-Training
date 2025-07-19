from math import inf
# Uses iterative bottom-up dynamic programming to build up to
# the optimal solution
def coin_change(coins: list[int], amount: int) -> int:
    n = amount
    # Generate the dp list, each index value representing a total amount from
    # zero to the target amount and element content representing the minimum
    # number of coins necessary to equal the index value. We only need a 1D list
    # because we can use each coin an unlimited number of times. Therefore, we
    # do not need to keep keep track of which coin was used when.
    dp = [inf for _ in range(n+1)]
    # Must set the base case to kick off the process
    dp[0] = 0 # Minimum number of coins to make zero is zero

    # Iteratively explore the state space
    for i in range(1, n+1): # Potential amounts
        # For every incremental target amount, we iterate through ALL coins
        # This is VERY important to keep in mind
        for coin in coins:
            # Only use the coin if its small enough to fit within the current
            # amount target
            if i - coin >= 0:
                # If the coin fits, we know we can look back to the number of
                # coins necessary to hit the incremental amount minus the
                # current coin's value and simply add one. This lets us hit the
                # current target with as few coins as possible! We take the min
                # of this trick and the current dp val since it may in fact be
                # smaller
                dp[i] = min(dp[i-coin] + 1, dp[i])
    return int(dp[-1]) if dp[-1] < inf else -1

if __name__ == "__main__":
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_change(coins, amount)
    print(res)
