mylist = [6,1,8,3,4,4,7,5,2,9]

from typing import List

# Bubble sort
# Repeatedly step through the list and compare adjacent pairs, swapping them if they are in
# the incorrect order.
# TC: O(n**2)
# SC: O(1)
def sort_list(unsorted_list: List[int]) -> List[int]:
    # Loop over the entire input list
    for i in range(0, len(unsorted_list) - 1): # Subtracting 1 because we access the last element in a later step
        # Compare elements and swap if they are in the incorrect order
        for trailing_index in range(0, len(unsorted_list) - i - 1):
            if unsorted_list[trailing_index] > unsorted_list[trailing_index+1]:
                unsorted_list[trailing_index], unsorted_list[trailing_index+1] = unsorted_list[trailing_index+1], unsorted_list[trailing_index]

    return unsorted_list

print(sort_list(mylist))
