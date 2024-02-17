import math

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
# Loops over the list repeatedly and compares each pair of adtrailing_indexacent items and then swaps them if they are in the wrong order
# Each full iteration moves the largest value in the list from wherever it is to the furthest right position it can occupy
# Therefore, we have one loop tha iterates over the length of the list and another that iterates over the length of the
# list that has not yet been fully sorted.  This allows us to perform the necessary number of iterations but also avoid
# pointlessly traversing to the end of the list each time
def bubbleSort(sort_list):
    for i in range(0, len(sort_list) -1): # Defines the entire length of the list. 
        for trailing_index in range(0, len(sort_list) - i - 1): # Defines the length of the list for which we have not yet sorted everything
            if sort_list[trailing_index] > sort_list[trailing_index+1]: # If the first value is greater than the second value then...
                sort_list[trailing_index], sort_list[trailing_index+1] = sort_list[trailing_index+1], sort_list[trailing_index] # Swap them
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
        for trailing_index in range(i+1, len(sort_list)): # Defines the section of the list that is unsorted
            if sort_list[min_index] > sort_list[trailing_index]: # If the value at the min index is actually greater than some value we've found in the unsorted section...
                min_index = trailing_index # Change that index to the one where we found that minimum value
        sort_list[i], sort_list[min_index] = sort_list[min_index], sort_list[i] # Swap those values 
    return sort_list



# Insertion Sort
# ---------------------------------------------------------------------
# TC: O(n^2) due to the nested loops
# SC: O(1) since sorting is in-place
# Similar to selection sort - the array is divided into two parts: sorted and unsorted.  The strategy is to take the first element
# from the unsorted part and find its correct position in the sorted part.  This process is repeated until the unsorted section is
# empty.  Sorted part of the list will be on the left hand side and unsorted on the right.
# Useful when there is a continuous inflow of numbers
def insertionSort(sort_list):
    for leading_index in range(1, len(sort_list)):
        leading_value = sort_list[leading_index]
        trailing_index = leading_index-1
        # Note: Withing the while loop, trailing index + 1 cannot be simplified to leading index here, because trailing index must 
        # be decremented n number of times backwards to traverse the sorted portion of the list.  If you replace trailing_index + 1
        # with leading_index, you'll get the same list out as you put in
        while trailing_index >=0 and leading_value < sort_list[trailing_index]: # Walk backwards (right to left) through the sorted part of the list until we've found the spot to insert our value
            sort_list[trailing_index+1] = sort_list[trailing_index] # Shift the one ahead to the one behind
            #print(leading_index, trailing_index, trailing_index + 1)
            trailing_index -= 1
        sort_list[trailing_index+1] = leading_value
    return sort_list


# Bucket Sort
# ---------------------------------------------------------------------
# TC: Depends on the sorting algorithm used.  O(n^2) here
# SC: O(n)
# With Bucket Sort, the efficiency is determined by the underlying algorithm we use to do the sorting.  All we do here is put the
# the data into buckets.
# Bucket sort can be more time efficient than O(n^2) but is only good if the numbers we're sorting are uniformly distributed.
#   Uniform - 1, 2, 3, 4, 8, 6, 7, 10, 9
#   Not uniform - 1, 2, 3, 55, 92, 10021, 82829
def bucketSort(sort_list):
    num_buckets = round(math.sqrt(len(sort_list)))
    max_list_val = max(sort_list) # We use this figure out which bucket a given element should fall within
    bucket_container = []
    return_list = []

    # Create the number of buckets we need
    for i in range(0, num_buckets):
        bucket_container.append([])

    # Loop through the sort_list and figure out which bucket each element should be in
    for element in sort_list:
        bucket = math.ceil(element * num_buckets/max_list_val) # The ceil function always rounds up to the next integer. (2.1 -> 3.0, for example)
        bucket_container[bucket-1].append(element) # Add the element to the appropriate bucket.  Subtracting 1 since list indexes start at 0.

    # Now, call the sorting algorithm of our choice to sort each bucket
    for bucket_num in range(num_buckets):
        bucket_container[bucket_num] = insertionSort(bucket_container[bucket_num])

    # We must now merge the sorted buckets
    for bucket_num in range(num_buckets):
        for item in range(len(bucket_container[bucket_num])):
            return_list.append(bucket_container[bucket_num][item])
    
    return return_list


# Testing
my_list = [2,1,7,6,5,3,4,9,8]
#print("\n\n Bubble Sort:")
#print(bubbleSort(my_list))

#print("\n\n Selection Sort:")
#print(selectionSort(my_list))

#print("\n\n Insertion Sort:")
#print(insertionSort(my_list))

print("\n\n Bucket Sort:")
print(insertionSort(my_list))