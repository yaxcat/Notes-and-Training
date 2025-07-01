def festival_game(target: list[int]) -> int:
    # Intialize DP table
    dp = [[0]*len(target) for _ in range(len(target))] # Holds the maximum score possible for a given interval

    def get_score(left, right):
        """
        Use interval dynamic programming to compute the maximum points that can be gained
        by optimally bursting all target balloons.
        
            Approach:
            - For any sub-interval [left, right], consider each possible balloon as the last one to burst in that interval.
            - The score for bursting balloon i last is determined by the value of target[i] and the adjacent (possibly virtual) balloons.
            - For each choice, recursively solve the sub-intervals to the left and right of i, then combine their maximal scores.
            - The DP table dp[left][right] records the best possible score obtainable for interval [left, right].
            - This approach ensures that overlapping subproblems are computed only once (memoization).
        
            Time complexity: O(n^3), with n = len(target)
            Space complexity: O(n^2)
        """
        # Return 0 for an invalid interval
        if left > right:
            return 0
        # If the maximum value for the interval has already been found, simply
        # return it
        if dp[left][right] != 0:
            return dp[left][right]
        # Iterate through every target balloon within the left and right interval (inclusive)
        for i in range(left, right+1):
            # Recursively explore the space between the left and right bounds and compute the
            # points for hitting that iterval.  Will recurse down to the left edge first
            left_interval = get_score(left, i-1)
            right_interval = get_score(i+1, right)
            # Calculate the value for hitting target[i]
            # If we've hit the beginning of the list there are no bounding balloons so 
            # the multiple is 1, otherwise it is the element to the left of the target
            left_multiplier = 1 if left == 0 else target[left-1]
            # If we've hit the end of the targets list, there are no bounding balloons
            # so the multiple is 1, otherwise it is the element to the right of the target
            right_multiplier = 1 if right == len(target)-1 else target[right+1]
            val = left_multiplier * target[i] * right_multiplier

            # Update the DP table for the current maximum possible score
            dp[left][right] = max(
                dp[left][right],
                left_interval + right_interval + val
            )
        return dp[left][right]

    # Run the program on the initial list of available targets.
    return get_score(0, len(target)-1)

if __name__ == "__main__":
    target = [int(x) for x in input().split()]
    res = festival_game(target)
    print(res)
