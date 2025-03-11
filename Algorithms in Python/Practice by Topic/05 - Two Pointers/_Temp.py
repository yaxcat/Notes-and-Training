from typing import List

def subarray_sum_fixed(nums: List[int], k: int) -> int:
    largest = 0
    window_sum = 0
    for right in range(0, k):
        largest += nums[right]
        window_sum += nums[right]
    for right in range(k, len(nums)):
        left = right-k
        window_sum -= nums[left]
        window_sum += nums[right]
        largest = max(largest, window_sum)
        
    return largest

if __name__ == "__main__":
    s = '1 2 3 7 4 1'
    nums = [int(x) for x in s.split()]
    k = 3
    res = subarray_sum_fixed(nums, k)
    print(res)
