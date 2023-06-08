# COLLECTIONS MODULE

# The collections module provides a doubly linked list data structures.  As a consequence, lements can be efficiently added or removed 
# from each each side of the list and it can be used for both queues and stacks.  It is unbounded by default but can be size
# constrained if desired.

# collections.deque as a FIFO queue
#_______________________________________________________________________________________________________________________________
from collections import deque

# Create the linked list object:
myqueue = deque(maxlen=3)

# Add some values:
myqueue.append('A')
myqueue.append('B')
myqueue.append('C') # Note that values are added to the end of list object

print("")
print(myqueue)
print("")

# If you add more elements than the list has room for, the first object is dropped and the element you are trying to add is appended
# to the end as usual
myqueue.append('D')

print("")
print(myqueue)
print("")


print("")
print(myqueue.popleft()) # Remove the first element of the queue from the list and return it
print(myqueue)
print("")

# queue as a FIFO queue
#_______________________________________________________________________________________________________________________________

import queue as q
myq = q.Queue(maxsize=3)

print("")
print("Queue Size:", myq.qsize())
print("")

# Add some values:
myq.put('A')
myq.put('B')
myq.put('C')
print("")
print("Queue Size:", myq.qsize())
print("")
# Remove some values:
print("")
print(myq.get())
print("Queue Size:", myq.qsize())
print("")