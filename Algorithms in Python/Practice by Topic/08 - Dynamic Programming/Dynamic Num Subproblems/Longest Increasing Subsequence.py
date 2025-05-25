from functools import lru_cache

"""
To solve this problem using top-down dynamic programming, we rely on two levels of looping: one outside the 
recursive function and one inside. The outer loop initiates a recursive search from every index in the input 
list. This is necessary because the longest increasing subsequence may start anywhere, and we need to evaluate 
all possible starting points to avoid missing the global optimum. The inner loop, defined within the recursive 
dfs function, explores the valid continuations of an increasing subsequence from the current index. 
Specifically, it checks all future indices to the right of the current one and recursively follows only those 
where nums[next] > nums[curr], ensuring the subsequence remains strictly increasing. You can think of the outer 
loop as evaluating the problem at the macro scale — identifying the globally longest sequence — while the inner 
loop handles the micro scale — finding the longest increasing path from a fixed starting point. Together, they 
traverse the full state space tree of possibilities without redundant recomputation, thanks to memoization.
"""

def longest_sub_len(nums: list[int]) -> int:
    n = len(nums)
    @lru_cache(maxsize=None) # Memoize
    def dfs(curr_ind):
        # Base case, we have reached the end of the list, so return 0
        # because there is no element at i == n
        if curr_ind == n:
            return 0
        # Initialize best and then recursively explore the sequence
        best = 1 # Current element counts
        # We use the loop because we must start from every element to ensure 
        # we do not miss any optimal sequences
        for next_ind in range(curr_ind+1, n): # Micro scale
            # Prune branches where the value at the next index is less than
            # that of the current because these branches don't have a valid
            # starting point given our current position. Explore the rest,
            # adding 1 for each valid element in the remaining sequence
            # we've explored so far
            if nums[next_ind] > nums[curr_ind]:
                best  = max(best, 1+dfs(next_ind))
        return best
    
    longest = 0 # Overall sequence
    for i in range(0, n): # Macro scale
        longest = max(longest, dfs(i))
    return longest

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    res = longest_sub_len(nums)
    print(res)
