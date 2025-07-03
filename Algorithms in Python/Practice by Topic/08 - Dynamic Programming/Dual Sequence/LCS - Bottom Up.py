# Uses a bottom up iterative approach to find the LCS
def longest_common_subsequence(word1, word2):
    n = len(word1)
    m = len(word2)

    # Initialize the DP table
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]    

    # Iteratively build up the LCS
    for i in range(0, n+1): # Loop over word1
        for j in range(0, m+1): # Loop over word2
            # Base case - if the prefix is of length zero, by definition
            # we cannot have a valid LCS
            if i == 0 or j == 0:
                dp[i][j] = 0
            # If we've found a matching character, increase the LCS by 1
            elif word1[i-1] == word2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            # If we have not, record the max possible by skipping the
            # character in word1 or word2 and move on
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[n][m]