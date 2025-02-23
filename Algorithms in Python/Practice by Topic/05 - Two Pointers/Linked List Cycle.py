class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
# Uses Floyd’s Cycle Detection Algorithm (Tortoise and Hare) to check if a linked 
# list has a cycle
def has_cycle(nodes: Node) -> bool:
    # Initialize fast (hare) and slow (tortoise) pointers at the head of the list
    hare = nodes
    tortoise = nodes
    # Move hare at twice the speed of tortoise. If a cycle exists, hare will "lap" 
    # tortoise.
    while hare and hare.next: # Ensure hare and hare.next exist to avoid NoneType errors
        hare = hare.next.next
        tortoise = tortoise.next
        # If the fast and slow pointers meet, a cycle is present
        if tortoise == hare:
            return True
    # If hare reaches the end of the list (None), no cycle exists
    return False

if __name__ == "__main__":
    s = '1 2 3 4 -1'
    raw_input = [int(x) for x in s.split()]
    nodes_list = []
    for i in range(len(raw_input)):
        nodes_list.append(Node(i))
    for i, entry in enumerate(raw_input):
        if entry != -1:
            nodes_list[i].next = nodes_list[entry]
    nodes = nodes_list[0]
    res = has_cycle(nodes)
    print("true" if res else "false")
