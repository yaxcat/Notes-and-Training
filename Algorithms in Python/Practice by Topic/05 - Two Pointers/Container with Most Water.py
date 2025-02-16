from typing import List
from math import inf
# Finds the maximum amount of water that could be stored between two
# heights in a list
def container_with_most_water(arr: List[int]) -> int:
    max_area = -inf
    left = 0
    right = len(arr)-1
     # Use two pointers to check all possible container widths
    while left < right:
        # The water level is limited by the shorter of the two heights
        height = min(arr[left], arr[right])
        width = right-left
        area = height * width
        # Update max_area if we've found a larger value
        if area > max_area:
            max_area = area
        # Search for a potentially larger area by advancing the pointer
        # of the smaller element.  This works because for an equal or smaller
        # width, the only way to get a greater area is to increase the height
        # of the smaller elements.
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    return max_area

if __name__ == "__main__":
    txt = '1 8 6 2 5 4 8 3 7'
    arr = [int(x) for x in txt.split()]
    res = container_with_most_water(arr)
    print(res)
