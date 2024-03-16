# See graphic for description of how code operates and limitations

# We only use BFS (and not DFS) for finding the shortest path because DFS by design traverses deeply into the graph and has
# a tendancy to go as far as possible from the source.  Therefore, it will never find the shortest path.

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    # TC: O(E) Not O(E + V) because we're only visiting connected vertices
    # SC: O(E) Because we're inserting the edges and vertices into memory, but the number of edges will always be greater 
    def bfs(self, sourceNode, targetNode):
        queue =[] # Used for maintaining paths, will continue to accumulate paths (sequences of vertices) as the function runs
        queue.append([sourceNode]) # Append the starting point so we can get started
        while queue:
                print("Queue: ", str(queue))
                path = queue.pop(0) # Pop the first path in the queue
                print("---Path: ", str(path))
                node = path[-1] # Get the last vertex in the path list, we need to start from here to continue exploring the graph
                print("------Node: ", str(node))
                if node == targetNode: # If we found our target, we can quit
                     return path
                # This loop allows us to continue exploring the graph, by finding the neighbors of the node we left off on during
                # the last cycle and characterizing its edges
                for neighbor_node in self.gdict.get(node, []) : # Get the neighbors of the current/last explored node or return an empty list
                     new_path = list(path) # Make a copy of the path we've mapped so far
                     new_path.append(neighbor_node) # Now add the new nodes we have mapped to that path
                     print("---------New Path: ", str(new_path))
                     queue.append(new_path) # Append our new map/path to the queue so that we can continue exploring it in the future to find our target if we need to.

my_dict = { "a" : ["b", "c"],
               "b" : ["d", "g"],
               "c" : ["d", "e"],
               "d" : ["f"],
               "e" : ["f"],
               "g" : ["f"]
            }

g = Graph(my_dict)
print(g.bfs('a', 'f'))