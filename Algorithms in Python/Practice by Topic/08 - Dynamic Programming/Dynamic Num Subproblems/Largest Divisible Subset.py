from functools import lru_cache

def find_largest_subset(nums: list[int]) -> int:
    # It is crucial to sort the list. Running the algorithm on a sorted list
    # results in a much simplified state space that looks something like the
    # longest path in a DAG. Because the numbers are ordered, we can process
    # the data like a chain of directed edges. If we didn't sort, the 
    # innocuous addition of an or operator in the constraint check would
    # explode the state space and result in a geometry that looks more like a
    # web. Time complexity would be brutal as a result.
    nums.sort()
    n = len(nums)
    @lru_cache(maxsize=None) # Memoize by current index value
    def dfs(curr_ind): 
        max_len = 1 # Every element can be a subset of size 1
        # For each index curr_ind, we examine all prior indices to find valid 
        # divisors. If nums[curr_ind] is divisible by nums[prev_ind], we can 
        # extend the chain ending at prev_ind. The recursive call explores the 
        # longest chain up to prev_ind, and we add 1 to include nums[curr_ind]
        for prev_ind in range(curr_ind):
            if nums[curr_ind] % nums[prev_ind] == 0: # Pairwise division constraint is satisfied
                max_len = max(max_len, 1+dfs(prev_ind))
        return max_len
    # Since any element could be the end of the largest divisible subset, we 
    # must evaluate the subset length ending at each index. The global maximum 
    # is the best of these.
    return max(dfs(i) for i in range(n))

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    res = find_largest_subset(nums)
    print(res)
