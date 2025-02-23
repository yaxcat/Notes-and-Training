from typing import List

def range_sum_query_immutable(nums: List[int], left: int, right: int) -> int:
    psum = [0]
    # Generate prefix sums for input list
    for num in nums:
        psum.append(psum[-1] + num)
    # Return sum for the query interval
    return psum[right+1] - psum[left] # Add 1 to right because psum is 1 element longer than the input list

if __name__ == "__main__":
    s = '1 2 3 4'
    nums = [int(x) for x in s.split()]
    left = 1
    right = 3
    res = range_sum_query_immutable(nums, left, right)
    print(res)
