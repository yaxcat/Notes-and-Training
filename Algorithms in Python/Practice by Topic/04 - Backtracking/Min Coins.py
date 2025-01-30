from typing import List
import math

def coin_change(coins: List[int], amount: int) -> int:
    def dfs(coins, amount, sum):
        # Base case
        if sum == amount:
            return 0
        if sum > amount:
            return math.inf
        
        ans = math.inf
        for coin in coins:
            result = dfs(coins, amount, sum+coin)
            if result == math.inf:
                continue
            ans = min(ans, result+1)
        return ans
    result = dfs(coins, amount, 0)
    return result if result != math.inf else -1

if __name__ == "__main__":
    txt = '1 2 5'
    coins = [int(x) for x in txt.split()]
    amount = 11
    res = coin_change(coins, amount)
    print(res)
