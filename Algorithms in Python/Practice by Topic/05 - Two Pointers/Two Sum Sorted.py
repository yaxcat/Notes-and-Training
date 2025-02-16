from typing import List
# Find two elements which add up to the target
def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    # Initialize the left and right pointers
    left = 0
    right = len(arr)-1
    # Iterate while the left pointer is to the left of the right pointer
    while left < right:
        # Compute the sum of the left and right indices, starting at the
        # extreme left and right boundaries
        total = arr[left] + arr[right]
        # If we've hit the target, we're done. Return the indices
        if total == target:
            return [left, right]
        # Since we initialized total using the largest and smallest possible
        # elements, we know that if total is less than the target, we must 
        # move the left pointer further right, and that if it is larger, we
        # must move the right pointer to the left
        elif total < target:
            left += 1
        elif total > target:
            right -= 1
    # If no suitable pair was found, return an empty list
    return []


if __name__ == "__main__":
    txt = '2 3 5 8 11 15'
    arr = [int(x) for x in txt.split()]
    target = 8
    res = two_sum_sorted(arr, target)
    print(" ".join(map(str, res)))
