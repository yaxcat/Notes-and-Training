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
    for i in range(0, len(sort_list) -1): # Defines the entire length of the list. 
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



# Insertion Sort
# ---------------------------------------------------------------------
# TC: O(n^2) due to the nested loops
# SC: O(1) since sorting is in-place
# Similar to selection sort - the array is divided into two parts: sorted and unsorted.  The strategy is to take the first element
# from the unsorted part and find its correct position in the sorted part.  This process is repeated until the unsorted section is
# empty.  Sorted part of the list will be on the left hand side and unsorted on the right.
def insertionSort(sort_list):
    # Start by iterating forwards (left to right) through the list
    for leading_index in range(1, len(sort_list)): # Start at 1 because we're comparing each element with the one leading it in the list
        leading_value = sort_list[leading_index]
        trailing_index = leading_index - 1
        # For each forward iteration, work backwards through the sorted part of the list looking for the correct spot to insert the
        # value found at the forward iteration.  This 'inserts' it in the sorted list.
        while trailing_index > 0 and leading_value < sort_list[trailing_index]: # While we have a valid list index and the leading value is greater than the trailing value...
            sort_list[leading_index] = sort_list[trailing_index] # Swap the values
            trailing_index -= 1 # Work backwards through the sorted section until we've found the right spot
        sort_list[leading_index] = leading_value # Set the leading value back to what it was
    return sort_list

# Testing
my_list = [2,1,7,6,5,3,4,9,8]
#print("\n\n Bubble Sort:")
#print(bubbleSort(my_list))

#print("\n\n Selection Sort:")
#print(selectionSort(my_list))

print("\n\n Insertion Sort:")
print(insertionSort(my_list))