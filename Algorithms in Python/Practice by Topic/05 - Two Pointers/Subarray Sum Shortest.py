from typing import List

# Finds the finds the shortest possible slice of the list whose elements
# are equal to or greater than the target. It is same to assume target will
# not exceed the sum of all elements in the list
def subarray_sum_shortest(nums: List[int], target: int) -> int:
    shortest = len(nums)
    left = 0
    window = 0
    total = 0
    # Use a sliding window to find the shortest subset of nums which meets
    # our criteria
    for right in range(0, len(nums)):
        # Increase window size and total as the window expands to the right
        window +=1
        total += nums[right]
        # If the running total is >= target, we know we might be
        # able to find a shorter slice of the list that still meets our 
        # criteria, so shrink the window from the left until the running
        # total is less than or equal to the target
        while total >= target:
            # Compute the shortest within the loop since any slice greater
            # than the target is potentially the solution
            shortest = min(shortest, window) 
            total -= nums[left]
            window -= 1
            left += 1
    return shortest

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    target = int(input())
    res = subarray_sum_shortest(nums, target)
    print(res)
