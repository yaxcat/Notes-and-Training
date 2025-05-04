from collections import Counter
from heapq import heapify, heappush, heappop
import sys

def reorganize_string(s: str) -> str:
    # Get the frequency distribution of the characters in the input string
    char_count = Counter(s)

    # If the count of any single character is over half the length of input string
    # we know it is impossible to re-arrange the string to meet the requirements
    for char in char_count:
        if char_count[char] > (len(s)+1)//2:
            return ""

    # Reverse key-value relationship so that we can heapify using character count
    # Use negative counts to build a max heap
    heap = [[-count, char] for char, count in char_count.items()]
    heapify(heap)

    result = []
    while len(heap) >= 2:
        # Pop two most frequently occuring letters from the heap
        char_1 = heappop(heap)
        char_2 = heappop(heap)
        # Update character counts and push back onto the heap if they're
        # greater than zero. If they're still the most frequently occuring,
        # they'll bubble back up to the top of the heap. We update the count 
        # in the heap, not the counter object because the character may 
        # re-enter the heap
        char_1[0] += 1 # Add instead of subtract because we negated char counts get max heap behavior
        if char_1[0] < 0: # Reverse inequality relationship too
            heappush(heap, char_1)
        char_2[0] += 1
        if char_2[0] < 0:
            heappush(heap, char_2)
        # We're popping unique characters and updating their counts separately
        # So it is safe to append in this fashion without causing a repeating
        # character sequence like 'aaaabc'
        result.append(char_1[1])
        result.append(char_2[1])

    # Handle final left over character, if any
    # Handle final leftover character, if any
    if heap:
        count, char = heap[0]
        if count != -1:
            return ""
        result.append(char)
    if len(result) != len(s):
        return ""
    return "".join(result)

if __name__ == "__main__":
    s = 'aab'
    res = reorganize_string(s)
    print(res)
    if not res:
        print("Impossible")
        sys.exit()
    input_counter, output_counter = Counter(s), Counter(res)
    if input_counter != output_counter:
        print("Not rearrangement")
        sys.exit()
    for i in range(len(res) - 1):
        if res[i] == res[i + 1]:
            print(f"Same character at index {i} and {i+1}")
            sys.exit()
    print("Valid")
