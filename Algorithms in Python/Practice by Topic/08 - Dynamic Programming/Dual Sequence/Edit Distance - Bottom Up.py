# Uses dynamic programming to build up a solution iteratively, from the bottom up
def min_distance(word1: str, word2: str) -> int:
    # Collect word dimensions
    n = len(word1)
    m = len(word2)
    # Initialize DP table
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    # Base cases
    for x in range(0, n+1):
        dp[x][0] = x # Would have to delete prefix from word1
    for x in range(0, m+1):
        dp[0][x] = x # Would have to insert prefix to word1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            # If the characters are the same, we can use the number of edits
            # from the last iteration, since no new edits need to be performed
            if word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1]
            # If the characters do not match, we have three choices:
            #   1. Insert character from word2 into word1
            #   2. Delete character from word1
            #   3. Replace a character in word1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
    # Last element will contain the solution
    return dp[n][m]

if __name__ == "__main__":
    word1 = 'amost'
    word2 = 'algomonster'
    res = min_distance(word1, word2)
    print(res)
