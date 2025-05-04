from heapq import heappush, heappop

def nth_ugly_number(n: int) -> int:
    heap = [1] # Initialize heap with first ugly number
    visited = set([1]) # Use a set to ensure that we don't add duplicate numbers to heap
    factors = [2, 3, 5]
    step = 0

    pop_chain = [] # For debugging
    
    # Continue calculating ugly numbers as long as we have not reached n
    while step < n:
        curr = heappop(heap)
        pop_chain.append(curr)
        # Increment by one when pop from the heap because it is the pop frequency that
        # correlates with finding the nth ugly number. We can safely generate the next
        # three ugly numbers for each popped value because the heap structure ensures
        # those larger numbers will stay lower down in the heap where they belong
        step += 1 
        # Loop over the prime factors and add the resultant ugly number to the heap and
        # set if it hasn't come up already
        for f in factors:
            next_val = curr * f
            if next_val not in visited:
                visited.add(next_val) # Ensures we dont get something 6, 6 since we have 2*3 and 3*2
                heappush(heap, next_val)
    #print(pop_chain)
    
    return curr


if __name__ == "__main__":
    n = 10
    res = nth_ugly_number(n)
    print(res)
