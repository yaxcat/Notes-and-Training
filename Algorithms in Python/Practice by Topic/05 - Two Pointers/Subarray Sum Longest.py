from typing import List
# Finds the length of the longest subarray with a sum smaller than
# or equal to the target
def subarray_sum_longest(nums: List[int], target: int) -> int:
    # Initialize tracking variables
    longest = 0
    left = 0
    total = 0
    length = 0
    # Loop over the length of the array, continuing to increase the
    # size of the window as long as the running total does not exceed
    # the target amount
    for right in range(0, len(nums)):
        total += nums[right]
        length += 1
        # Use a while loop to shift the left pointer rightward until
        # the running total is less than or equal to the target. Use
        # a while loop rather than an if statement because we may need
        # to drop multiple elements from left side of the window
        while total > target:
            longest = max(longest, length-1)
            total -= nums[left]
            left += 1
            length -= 1
    return longest

if __name__ == "__main__":
    txt = '1 6 3 1 2 4 5'
    nums = [int(x) for x in txt.split()]
    target = 10
    res = subarray_sum_longest(nums, target)
    print(res)
