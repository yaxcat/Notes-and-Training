def min_distance(word1: str, word2: str) -> int:
    # Collection word dimensions
    n = len(word1)
    m = len(word2)

    # Initialize DP table
    dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

    def dfs(i, j):
        # Base case 1 - # Need to insert remaining characters in word2
        if i == n:
            dp[i][j] = m - j
            return dp[i][j]
        # Base case 2 - # Need to delete remaining characters in word1
        if j == m:
            dp[i][j] = n - i
            return dp[i][j]
        # Check the memo to reduce time complexity
        if dp[i][j] != -1:
            return dp[i][j]

        # If the characters match, proceed with exploration of the rest
        # of the words.
        if word1[i] == word2[j]:
            dp[i][j] = dfs(i+1, j+1)
            return dp[i][j]
        # If the characters do not match
        else:
            replace = dfs(i+1, j+1) + 1 # Replace char in word1
            remove_i = dfs(i+1, j) + 1 # Delete char in word1
            remove_j = dfs(i, j+1) + 1 # Insert char in word1
            dp[i][j] = min(replace, remove_i, remove_j)
            return dp[i][j]

    return dfs(0, 0)

if __name__ == "__main__":
    word1 = input()
    word2 = input()
    res = min_distance(word1, word2)
    print(res)
