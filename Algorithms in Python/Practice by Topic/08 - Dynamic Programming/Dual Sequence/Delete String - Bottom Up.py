# Uses a bottom up approach to calculate the minimum possible 
# deletion cost
def delete_string(costs: list[int], s1: str, s2: str) -> int:
    n = len(s1)
    m = len(s2)
    a_ind = ord('a') # 97

    # Initialize DP table. Max string len is 1000, so set to
    # 1001 by default
    dp = [[0]*1001 for _ in range(1001)]

    # Base cases - 
    # S1
    for x in range(1, n+1): # Deletion cost for each prefix in s1
        dp[x][0] = dp[x-1][0] + costs[ord(s1[x-1])-a_ind] # Cost of deleting all chars in s1[:x]
    # S2
    for x in range(1, m+1):
        dp[0][x] = dp[0][x-1] + costs[ord(s2[x-1])-a_ind] # Cost of deleting all chars in s2[:x]

    for i in range(1, n+1):
        for j in range(1, m+1):
            # Characters are the same
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] # No deletion necessary, so cost is unchanged
            else:
                # Take the minimum of deleting letters from s1
                # or s2 and account for the cost of each deletion
                dp[i][j] = min(
                    dp[i][j-1] + costs[ord(s2[j-1])-a_ind],
                    dp[i-1][j] + costs[ord(s1[i-1])-a_ind]
                )
    return dp[n][m]

if __name__ == "__main__":
    costs = [1,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    s1 = 'aab'
    s2 = 'baa'
    res = delete_string(costs, s1, s2)
    print(res)
