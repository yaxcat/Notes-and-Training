
import math

# LINEAR SEARCH
# Just loops over an array/list and looks for a value.  Can be more efficient with sorted arrays
# TC: O(n)
# SC: O(1)

# In this version we return the index the value is located at
def linearSearch(search_list, target):
    list_length = len(search_list)
    for i in range(0, list_length):
        if search_list[i] == target:
            return i
    return -1 # If the target is not in the list


# BINARY SEARCH
# TC: O(LogN)
# SC: O(1)
# Much faster than Linear Search - eliminates half the candidates in each iteration instead of 
# eliminating them one by one.  However, it only works on sorted arrays/lists.
def binarySearch(search_list, target):
    # Define key indices we'll need to navigate the list. Initially, they will be based on the whole list
    start_ind = 0
    end_ind = len(search_list) - 1
    mid_ind = math.floor((start_ind + end_ind)/2) # No decimals in this house
    print(start_ind, mid_ind, end_ind)

    # Now loop through the array until the middle index contains the value we're looking for
    while not(search_list[mid_ind] == target) and start_ind <= end_ind: # The clause after the 'and' prevents an infinite loop if the target is not actually present in the search list
        # Slice the searchable part of the list in half with each iteration by adjusting the pointers
        if target < search_list[mid_ind]:
            end_ind = mid_ind - 1
        else:
            start_ind = mid_ind + 1
        mid_ind = math.floor((start_ind + end_ind)/2)
    print(start_ind, mid_ind, end_ind)

    if search_list[mid_ind] == target:
        return mid_ind
    else:
        return -1

my_list = [8,2,3,7,1,0,4,5,6]
my_sorted_list = [8,9,12,15,17,19,20,21,28]

#print("\n\nRunning Linear Search")
#print(linearSearch(my_list, 0))

print("\n\nRunning Binary Search")
print("Index - ", binarySearch(my_sorted_list, 16))