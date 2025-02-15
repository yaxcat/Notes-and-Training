from typing import List

# [1, 0, 2, 0, 0, 7] Input
# [1, 2, 7, 0, 0, 0] Output
# Moves 0s to the end of the list while preserving the relative
# order of non-zero elements. Performs the operation in place.
def move_zeros(nums: List[int]) -> None:
    slow = 0 
    # Loop over the length of the input list. Both fast and slow
    # pointers initially point at the same element. This is OK even
    # if it is non-zero since the swap doesn't do anything in this 
    # case
    for fast in range(0, len(nums)):
        # If the fast pointer is pointing at a non-zero element,
        # swap them and advance the slower pointer by 1. If both
        # point at non-zero elements, it will be the same element
        # and the swap will not do anything
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1



if __name__ == "__main__":
    txt = '1 0 2 0 0 7'
    nums = [int(x) for x in txt.split()]
    move_zeros(nums)
    print(" ".join(map(str, nums)))
