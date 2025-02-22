from typing import List
from typing import List

# Finds the subarray that sums to the target and returns its bounding indices.
def subarray_sum_total(arr: List[int], target: int) -> List[int]:
    # We must initalize with 0:0 because when the target sum is found starting at index 0, 
    # {0:0} ensures the function can correctly return [0, end_index]
    prefix_sum = {0: 0}  # Maps cumulative sums to their corresponding indices.
    running_total = 0
    ind = 0
    ans = []
    # Compute prefix sums while iterating through the list.
    for num in arr:
        ind += 1
        running_total += num
        # The key idea is that if there exists a previous prefix sum such that
        # subtracting it from the current running total gives the target sum,
        # then the subarray between those two indices sums to the target.
        complement = running_total - target
        if complement in prefix_sum:
            ans.append([prefix_sum[complement], ind])  # Return the start and end indices.

        # Store the running total with its corresponding index for future lookups.
        prefix_sum[running_total] = ind
    return ans

if __name__ == "__main__":
    s = '10 5 -5 -20 10'
    arr = [int(x) for x in s.split()]
    target = -10
    res = subarray_sum_total(arr, target)
    print(" ".join(map(str, res)))
