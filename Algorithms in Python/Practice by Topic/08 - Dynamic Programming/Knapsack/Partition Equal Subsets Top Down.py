# Use top down dynamic programming to determine whether or not
# partitioning of an array into two lists that sum to the same value
# is possible
def can_partition(nums: list[int]) -> bool:
    # If the list total cannot be evenly divided we know it cannot
    # be partitioned equally
    if sum(nums) % 2 != 0:
        return False
    
    n = len(nums)
    half_total = sum(nums)//2
    memo = {}

    def dfs(ind, curr_total):
        if (ind, curr_total) in memo:
            return memo[(ind, curr_total)]
        # Base case 1 - we have found a way to partion the list equally
        if curr_total == half_total:
            return True
        # Base case 2 - we have traversed the entire list and have
        # been unable to partition it equally or we've exceeded the
        # partition value, so prune away
        if ind == n or curr_total > half_total:
            return False
        
        # To recursively explore the partioning possibilities, we can either
        # skip the current item or take it and account for its value
        skip = dfs(ind+1, curr_total)
        take = dfs(ind+1, curr_total+nums[ind])

        # Memoize the results to reduce time complexity. Note the we memoize
        # the result of the recursive exploration of sub-branches leading to
        # the current state. In effect we are aggregate the results of the sub
        # problems at our current level of recursion. If we tried to memoize
        # the individual path results (skip and take separately) we would break
        # the crucial aggregation and return incorrect results.
        memo[(ind, curr_total)] = skip or take

        return memo[(ind, curr_total)]

    return dfs(0, 0)

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    res = can_partition(nums)
    print("true" if res else "false")
