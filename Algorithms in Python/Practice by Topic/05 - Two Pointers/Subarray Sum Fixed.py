from typing import List
# Uses a sliding window to efficiently find the largest sum
# possible given a window size, K
def subarray_sum_fixed(nums: List[int], k: int) -> int:
    largest_sum = 0
    window_total = 0
    # Loop over the input list
    for right in range(0, len(nums)):
        left = right-k # Calculate the left boundary of the window
        window_total += nums[right] # Iteratively add the rightmost value to the total
        # If the left pointer is non-negative, the right pointer has advanced a
        # distance of k, and the window has been fully formed. Begin iteratively
        # dropping the leftmost element to maintain an accurate window size
        if left >= 0:
            window_total -= nums[left]
            largest_sum = max(largest_sum, window_total)
    return largest_sum

if __name__ == "__main__":
    txt = '1 2 3 7 4 1'
    nums = [int(x) for x in txt.split()]
    k = 3
    res = subarray_sum_fixed(nums, k)
    print(res)
