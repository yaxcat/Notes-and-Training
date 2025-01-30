def decode_ways(digits: str) -> int:
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Initialize a dictionary to quickly determine if a letter can be found
    # at a digit
    lookup  = {str(i+1):letter for i, letter in enumerate(letters)}
    # Initialize another dictionary to hold previously computed results as
    # we recurse through the input digits
    memo = {}
    # Repeatedly slice the input digits and build a tree of valid codes as
    # we recurse on the list
    def dfs(start):
        # Base case - If we have reached the end of the input string, we have
        # hit a leaf node. This indicates all prior dfs() calls yeilded a 
        # valid code
        if start == len(digits):
            return 1
        # Check to see if the value at the current starting position has
        # already been computed
        if start in memo.keys():
            return memo[start]
        total = 0 # Initialize variable which holds the total number of valid decode strings
        # Slice the input digits to look for valid ways to decode it. Passing 
        # the end of each iteration into subsequent recursive calls allows the
        # fn to pick up where the calling fn left off
        for end in range(start+1, len(digits)+1):
            prefix = digits[start:end]
            # If the current digits slice is present in the lookup dict, it
            # represents a valid way to decode the digits, so call dfs again
            # to explore branches from this node
            if prefix in lookup.keys():
                total += dfs(end) # Running total is incremented every time we hit a leaf node (base case)
        memo[start] = total # Update the memo 
        return total # Bubble the result up the call stack
    return dfs(0)


if __name__ == "__main__":
    digits = input()
    res = decode_ways(digits)
    print(res)
