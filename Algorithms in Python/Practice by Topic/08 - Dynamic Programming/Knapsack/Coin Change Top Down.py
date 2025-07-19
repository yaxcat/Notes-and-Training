from typing import List
from math import inf
# Uses top down dynamic programming to find the minimum number of coins
# needed to hit a target value
def coin_change(coins: List[int], amount: int) -> int:
    memo = {} # Memoize to reduce time complexity
    # Performs DFS to explore the state space
    def helper(path_total):
        # Base case 1 - if we've hit the target, return 0 since we do
        # not need to add any more coins
        if path_total == amount:
            return 0
        # Base case 2 - if we've exceeded the target, this branch is
        # invalid, so return inf which we will use to avoid further
        # exploration
        if path_total > amount:
            return inf
        # The path total so far is the state which captures a sufficient
        # amount of detail return the minimum number of coins so far. In
        # other words, if we know the path total, we know the corresponding
        # minimum
        if path_total in memo:
            return memo[path_total]
        answer = inf # Initialize branch specific min number of coins
        # Recursively explore options for adding coins
        for coin in coins:
            branch_result = helper(path_total+coin) # Running total value of coins on this branch
            # Skip invalid branches
            if branch_result == inf:
                continue
            # Compare local branch minimum to the aggregate minimum found so far
            answer = min(answer, branch_result+1)
        memo[path_total] = answer # Memo is updated during recursive unwinding
        return memo[path_total]

    f = int(helper(0))

    return f if f < inf else -1

if __name__ == "__main__":
    coins = [int(x) for x in input().split()]
    amount = int(input())
    res = coin_change(coins, amount)
    print(res)
