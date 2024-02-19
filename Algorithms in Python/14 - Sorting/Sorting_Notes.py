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

# Merge Sort
# ---------------------------------------------------------------------
# TC: O(n(logN))
# SC: O(N) because of all the subarrays
# Merge sort works by continually dividing the list in half; it is a divide-and-conquer algorithm.  Once elements in the list have been atomized 
# using this process, they are merged back together into a single list.  Ordering is achieved by identifying the higher and lower values 
# during each step in the merging process.  The number of elements in each array decreases by roughly half during each division until single
# elements are obtained.  This is reversed during the merger step, with the number of elements in each array roughly doubling during each step
# in the aggregation process.  The elements are merged back into their original container at each step until they all wind up back in the orginal
# container.  Useful when you need stable sorting or lower time complexity.  Not good if space is a concern.

# A helper function is needed for mergeSort
# TC: O(n) # Since we have to loop through all elements in the array
def merge(sort_list, l, m, r): # l, m, and r are indices which identify the start, middle and end of the list
    # Calulate the number of elements that will be in each of the sub arrays once we divide sort_list
    left_array_elems = m - l + 1
    right_array_elems = r - m
    
    # Create the subarrays
    left_array = [0] * left_array_elems
    right_array = [0] * right_array_elems

    # Populate the subarrays with data from the list we want to sort
    for elem_num in range(0, left_array_elems):
        left_array[elem_num] = sort_list[l + elem_num] # Make sure to add the starting index value so that we grab the correct values from sort_list
    for elem_num in range(0, right_array_elems):
        right_array[elem_num] = sort_list[m + 1 + elem_num]

    # Define indices of the lists so that we can begin merger process
    i = 0 # initial index of left sub array
    j = 0 # initial index of right sub array
    k = l # initial index of merged sub array

    # Iterate over our subarrays to merge and sort them
    while i < left_array_elems and j < right_array_elems: # While our indexes are less the size of the subarrays...
        if left_array[i] <= right_array[j]: # if the element from the left array is smaller...
            sort_list[k] = left_array[i] # then put that element in the spot in sort_array
            i += 1
        else:
            sort_list[k] = right_array[j] # otherwise use the element from the right array, since it is smaller
            j += 1
        k += 1

    # After the sorting step, there may be elements in either subarray/list left over because the left and right subarrays may have differing
    # numbers of elements.  Thefore, we need to loop through any leftovers and add them to the merged list
    while i < left_array_elems:
        sort_list[k] = left_array[i]
        i += 1
        k += 1
    while j < right_array_elems:
        sort_list[k] = right_array[j]
        j += 1
        k += 1


def mergeSort(sort_list, l, r): # Start and end of the list that needs to be sorted
    # if we're not at the end of the list, find the middle index
    if l < r:
        m = (l + (r-1))//2 # use floor division since we want an integer
        
        # call the function recursively so that we can atomize the input list and merge it back together again
        mergeSort(sort_list, l, m) # Left subarray
        mergeSort(sort_list, m+1, r) # Right subarray add 1 to m since the m index is included in the left subdivision
        merge(sort_list, l, m, r) # Do the work
    return sort_list



# Quick Sort
# ---------------------------------------------------------------------
# Quick sort uses a strategy of comparing a pilot number chosen at random to all the other values in the list/array
# The array is sorted by iteratively swapping values based on a comparison to the pilot number.  That pilot number
# is then used as a boundary, which delineates the division between an area of the array with values less than the 
# pilot (left side) and area where values are greater than the pilot (right side).

# Function to swap list values
def swap(das_list, index_1, index_2):
    das_list[index_1], das_list[index_2] = das_list[index_2], das_list[index_1]

# Pivot - 
# With pivot, our goal is to find values less than the pilot number and swap them with numbers greater than the the
# pilot.  Then, we will swap the pilot number with the swap index number to form the boundary in the array.
def pivot(sort_list, pivot_index, end_index):
    # When we start, pivot and swap indexes will both point to the first element in the list
    swap_index = pivot_index
    # Now we iterate over the list to begin swapping values
    for i in range(pivot_index+1, end_index+1): # Add 1 to where we start because we we're comparing all other list items to the pivot element and we don't need to compare it to itself.  Add 1 to the end because need to analyze that last element (Python is non-inclusive)
        # By doing nothing to swap_index if the value we encounter is greater than the pilot value, we ensure that no matter what
        # the distribution of numbers in the array we're sorting looks like, or how close to the 'middle' of the distribution the pilot
        # is, we'll always conclude with the pilot value separating the smaller elements from the larger ones.
        if sort_list[i] < sort_list[pivot_index]: # If element in the list we're currently looking at is less than the pivot value...
            swap_index += 1 # Move the swap index up to the next element.  This will point to an element bigger than the pivot value
            swap(sort_list, swap_index, i) # Now we can swap those values so that smaller one is closer to the pilot (left) and the larger one is closer to the end (right)
    
    # Once we've reached the end of the list, all comparisons against the pilot value are done, so we swap the pilot
    # value with the pivot value.  Upon doing so, all values smaller than pilot will be to its right, and all values
    # larger will be to its left.
    swap(sort_list, pivot_index, swap_index)
    return swap_index # we need this since it will be our boundary

# Runs pivot recursively, using the index returned by pivot to continuously subdivide the list into smaller and smaller sorted chunks
def quickSort(sort_list, left_index, right_index):
    # Base case
    if left_index < right_index: # When left index == right index, its sorted, so we can stop
        print("L:", left_index)
        print("R:", right_index)
        print("\n")
        pivot_index = pivot(sort_list, left_index, right_index) # Run pivot once to split the list in half and find our boundary/pivot index
        # Now, run quicksort recursively until the list is sorted
        quickSort(sort_list, left_index, pivot_index-1) # Sort the left hand side of the list.  Subtract 1 from pivot since its our boundary and we don't want to include it
        quickSort(sort_list, pivot_index+1, right_index) # Sort the right hand side of the list.
    return sort_list




# Testing
my_list = [2,1,7,6,5,3,4,9,8]
my_new_list = [3,5,0,6,2,1,4]
#print("\n\n Bubble Sort:")
#print(bubbleSort(my_list))

#print("\n\n Selection Sort:")
#print(selectionSort(my_list))

#print("\n\n Insertion Sort:")
#print(insertionSort(my_list))

#print("\n\n Bucket Sort:")
#print(bucketSort(my_list))

#print("\n\n Merge Sort:")
#print(mergeSort(my_list, 0, 8))

print("\n\n Quick Sort:")
print(quickSort(my_new_list, 0, 6))
print(my_new_list)

