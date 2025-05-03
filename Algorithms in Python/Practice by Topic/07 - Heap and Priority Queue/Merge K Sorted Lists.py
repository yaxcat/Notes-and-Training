from heapq import heapify, heappush, heappop

# Takes advantage of the fact that the individual sublists are sorted by using a minimum
# heap to implement a priority queue which returns a globally sorted list of all 
# elements within the sublists
def merge_k_sorted_lists(lists: list[list[int]]) -> list[int]:
    results = []
    heap = []
    # Initialize the heap with the first value in each of the input lists
    # The number of elements in the heap at each iteration will be at most
    # equal to the number of lists (k). It will drop below k towards completion
    # as nodes are popped and the lists are exhausted
    for current_list in lists:
        # Key by first element value, data being the list and pointer
        heappush(heap, (current_list[0], current_list, 0))
    # Note that the heap is acting a lot like a queue in that as we pop
    # the smallest element, we add the next largest element for that list
    # to be processed later. It is this mechanism (priority queue) which allows us 
    # to return a globally sorted list
    while heap:
        val, current_list, head_index = heappop(heap)
        results.append(val)
        head_index += 1 # Move the pointer to the next element in the list
        # If the pointer is within bounds, add the next largest element of this list to the heap
        if head_index < len(current_list):
            heappush(heap, (current_list[head_index], current_list, head_index))
    return results



if __name__ == "__main__":
    lists = [[1, 3, 5], [2, 4, 6], [7, 10]]
    res = merge_k_sorted_lists(lists)
    print(" ".join(map(str, res)))
