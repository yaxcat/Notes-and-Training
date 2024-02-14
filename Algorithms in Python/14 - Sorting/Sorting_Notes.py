# SORTING

# There are two types of sorting that differ by:
#   1) Space used
#       - In place - Algorithm does not require any extra space for sorting (bubble sort)
#       - Out of place - Requires extra space to sort (merge sort)
#   2) Stability
#       - Stable - The order of similar/identical values is preserved (dupes stay in the same place relative to one another)
#       - Unstable - Order is not preserved

# Terminology:
#   1) Increasing order - each successive element is greater than the previous one
#       - Ex. 1, 3, 5, 7, 9, 11
#   2) Decreasing order - each successive element is less than the previous one
#       - Ex. 11, 9, 7, 5, 3, 1
#   3) Non increasing order - each successive element is less than or equal to its previous element
#       - Ex. 11, 9, 7, 5, 3, 3, 1
#   4) Non decreasing order - each successive element is greater than or equal to its previous element
#       - Ex. 1, 3, 5, 7, 7, 9, 11


# Bubble Sort
# ---------------------------------------------------------------------
# TC: O(n^2) due to the nested loops
# SC: O(1) since sorting is in-place
# Also sometimes referred to as Sinking Sort
# Loops over the list repeatedly and compares each pair of adjacent items and then swaps them if they are in the wrong order
# Each full iteration moves the largest value in the list from wherever it is to the furthest right position it can occupy
# Therefore, we have one loop tha iterates over the length of the list and another that iterates over the length of the
# list that has not yet been fully sorted.  This allows us to perform the necessary number of iterations but also avoid
# pointlessly traversing to the end of the list each time
def bubbleSort(sort_list):
    for i in range(0, len(sort_list) -1): # Defines the entire length of the list
        for j in range(0, len(sort_list) - i - 1): # Defines the length of the list for which we have not yet sorted everything
            if sort_list[j] > sort_list[j+1]: # If the first value is greater than the second value then...
                sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j] # Swap them
    return sort_list



# Selection Sort
# ---------------------------------------------------------------------
# TC: O(n^2) due to the nested loops
# SC: O(1) since sorting is in-place
# Strategy is to repeatedly find the minimum element and then move it to the sorted part of the array which graducally makes the
# unsorted part sorted.  The algorithm works iteratively and swaps the minimum value found in any given iteration with the first 
# value in the unsorted part of the array.  The sorted part of the array increases by 1 with each iteration, while the unsorted
# part decreases by the same amount.  Similar mechanics and drawbacks to Bubble Sort.
def selectionSort(sort_list):
    for i in range(0, len(sort_list)): # Defines the length of the entire list
        min_index = i
        for j in range(i+1, len(sort_list)): # Defines the section of the list that is unsorted
            if sort_list[min_index] > sort_list[j]: # If the value at the min index is actually greater than some value we've found in the unsorted section...
                min_index = j # Change that index to the one where we found that minimum value
        sort_list[i], sort_list[min_index] = sort_list[min_index], sort_list[i] # Swap those values 
    return sort_list




# Testing
my_list = [2,1,7,6,5,3,4,9,8]
print("\n\n Bubble Sort:")
print(bubbleSort(my_list))

print("\n\n Selection Sort:")
print(bubbleSort(my_list))