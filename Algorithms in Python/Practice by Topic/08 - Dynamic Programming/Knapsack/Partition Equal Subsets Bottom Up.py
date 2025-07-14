# Uses an iterative bottom up dynamic programming approach to determine
# partition feasibility
def can_partition(nums: list[int]) -> bool:
    # If we cannot divide the total sum of the list evenly, it is not
    # possible to partition it according to the constraints
    if sum(nums)%2 != 0:
        return False
    # Calculate the dp grid dimensions
    n = len(nums)
    m = sum(nums)//2
    # Generate the dp grid
    # X axis: all possible values between 0 and the partition size
    # Y axis: all possible elements from the input list
    dp = [[False for _ in range(m+1)] for _ in range(n+1)]
    dp[0][0] = True # Initial state, we can make a weight 0, with 0 elements
    # Loop over the dp matrix and assess partition feasibility. Rather
    # than testing each element-total combination to see if it is equal
    # to our target weight as with the top-down approach, we will start
    # at the simplest case and see if it is possible to build up to the
    # target weight using any of the configurations of list elements.
    for i in range(1, n+1): # List elements
        for j in range(m+1): # Partition values, must include 0 since it is a valid weight
            # If our current total weight is less than the previous list
            # element just use the previous computation result because
            # If we couldn't do it before, we can't do it now since we 
            # can't use this big new number.
            if j < nums[i-1]:
                dp[i][j] = dp[i-1][j]
            # Otherwise, we can use the previous computation or assess
            # the feasibility of combining a lesser weight with our current
            # element.  We check dp[i-1][j - nums[i-1]] because if we could 
            # build j - nums[i-1] before, then by adding nums[i-1], we can now 
            # reach j 
            else:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
    return dp[n][m]

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    res = can_partition(nums)
    print("true" if res else "false")
