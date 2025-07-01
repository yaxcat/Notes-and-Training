def lcs(i, j, word1, word2, memo):
    # Base case, if we're at the very beginning of a subsequence, by
    # definition, we cannot have a match
    if i == 0 or j == 0:
        return 0
    
    # Check memo to reduce time complexity
    if memo[i][j] != -1:
        return memo[i][j]

    # As recursive calls are pushed to the call stack we will start at 
    # the end (right) of each word and work backwards over the strings 
    # until we hit the base case. In effect we are slicing the input 
    # strings into smaller and smaller sets. During unwinding, we begin
    # at the start of each string (left) and build up the final result
    # as we traverse the state space tree. 
    result = 0
    # Common character found, subtract 1 due to 0 based indexing
    if word1[i-1] == word2[j-1]:
        # Recursively explore the remainder of each string
        result = lcs(i-1, j-1, word1, word2, memo) + 1
    # Recursively explore the result of skipping either the current letter
    # in word1 or the current letter in word2
    else:
        result = max(lcs(i-1, j, word1, word2, memo), lcs(i, j-1, word1, word2, memo))

    # Memoize result for faster runtime
    memo[i][j] = result
    return result


def longest_common_subsequence(word1: str, word2: str) -> int:
    n = len(word1)
    m = len(word2)
    memo = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    result = lcs(n, m, word1, word2, memo)
    return result

if __name__ == "__main__":
    word1 = input()
    word2 = input()
    res = longest_common_subsequence(word1, word2)
    print(res)
