class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Naive implementation
def middle_of_linked_list1(head: Node) -> int:
    # Loop through the linked list once to find its legnth
    num_nodes = 0
    node = head
    while node:
        node = node.next
        num_nodes += 1 
    # Compute the mid point and now loop through again until
    # hitting middle node and returning its value
    return_ind = num_nodes//2 + 1
    current_node = 1
    node = head
    while node:
        if current_node == return_ind:
            return node.val
        node = node.next
        current_node += 1

# Clever implementation using two pointers
def middle_of_linked_list2(head: Node) -> int:
    # Initially, point both the fast and slow nodes at the head
    slow_node = head 
    fast_node = head
    node_count = 1
    # Because we want to return middle element, we advance the
    # slow node pointer at half the rate of the fast node pointer
    while fast_node:
        fast_node = fast_node.next
        if node_count % 2 == 0:
            slow_node = slow_node.next
        node_count += 1
    # Once we've reached the end of list, we can simply return 
    # the value at the slow node pointer since we know its in
    # the middle of the list
    return slow_node.val

def build_list(nodes, f):
    val = next(nodes, None)
    if val is None:
        return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)

if __name__ == "__main__":
    txt = '0 1 2 3 4'
    head = build_list(iter(txt.split()), int)
    res = middle_of_linked_list1(head)
    print(res)
