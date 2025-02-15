from typing import List

def remove_duplicates(arr: List[int]) -> int:
    # Initialize the two pointers, both will move in the
    # same direction from left to right
    slow = 0
    fast = 0
    # Assuming the input list is not empty, there will always be
    # at least one unique entry
    unique_entries = 1
    # Loop over the entire length of the input list
    for fast in range(len(arr)):
        # If a new unique element is found, update the array in-place
        if arr[slow] != arr[fast]:
            unique_entries += 1 
            slow += 1
            arr[slow] = arr[fast]
    return unique_entries

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = remove_duplicates(arr)
    print(" ".join(map(str, arr[:res])))
