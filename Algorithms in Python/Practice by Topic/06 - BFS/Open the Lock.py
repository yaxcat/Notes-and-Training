from typing import List
from collections import deque

# Uses an implicit graph to find the minimum number of moves from the starting point '0000' to the 
# target combination
def num_steps(target_combo: str, trapped_combos: List[str]) -> int:
    # Each wheel can rotate forward or backward by one digit, with wraparound (9 -> 0 and 0 -> 9).
    # We use these dictionaries to model how each digit changes when rotated.
    # next_digit maps each digit to its clockwise neighbor.
    # prev_digit maps each digit to its counterclockwise neighbor.
    next_digit = {**{str(i):str(i+1) for i in range(9)}, '9':'0'}
    prev_digit = {edge:node for node, edge in next_digit.items()}

    # If we're lucky enough that our target combo is starting combo, we don't need to make any
    # moves
    if target_combo == '0000':
        return 0
    # Convert the list to a set for faster O(1) lookups when checking deadends.
    trapped_combo_set = set(trapped_combos)
    steps = {'0000':0}
    q = deque(['0000'])
    while len(q) > 0:
        curr_node = q.popleft()
        # Try turning each of the 4 wheels forward or backward to generate neighboring combinations.
        for i in range(0, 4):
            # Ex if we want to change the third digit in '0000'
            # '00' + '0'->'1' + '0' = '0010'
            new_combo = curr_node[0:i]+next_digit[curr_node[i]] + curr_node[i+1:] # Forward
            # Check to see if the combination already exists; if it does, it means that we have
            # visited this node previously, and if it is a dead end we must not add it
            if new_combo not in trapped_combo_set and new_combo not in steps:
                q.append(new_combo)
                # Keep track of the number of levels traversed within the dictionary, rather than
                # externally, as done in other problems
                steps[new_combo] = steps[curr_node] + 1
                # Check to see if we hit our target
                if new_combo == target_combo:
                    return steps[new_combo]
            # Ex if we want to change the third digit in '0000'
            # '00' + '0'->'9' + '0' = '0090'
            new_combo = curr_node[0:i]+prev_digit[curr_node[i]]+curr_node[i+1:] # Backward
            if new_combo not in trapped_combo_set and new_combo not in steps:
                q.append(new_combo)
                steps[new_combo] = steps[curr_node] + 1
                if new_combo == target_combo:
                    return steps[new_combo]
    return -1

if __name__ == "__main__":
    target_combo = input()
    trapped_combos = input().split()
    res = num_steps(target_combo, trapped_combos)
    print(res)
