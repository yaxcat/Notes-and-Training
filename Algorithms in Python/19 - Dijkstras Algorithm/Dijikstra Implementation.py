# Implementation is much less messy if we just use a few classes

# Dijikstra's algorithm does not work with negative numbers
# Negative cycle:
#   - Cycle - a path which allows you to start from and return to the same vertex (a loop)
#   - Negative cycle weight - the total weight of the path is negative
# Dijikstra will keep hitting this path over and over because the cost keeps getting lower each
# time, will run to inifinity


import heapq # Just use the standard Python library to make things easier

class Edge:
    def __init__(self, edge_weight, start_vertex, end_vertex):
        self.edge_weight = edge_weight
        self.start_vertex = start_vertex
        self.end_vertex = end_vertex

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False 
        self.predecessor = None
        self.neighbors = [] # Defines the topology around this node, made of edges
        self.min_distance = float("inf") # Set to inifinity initially since we're trying to find the shortest path

    # Need to override the inbuilt function so that we can compare node distances
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
    
    # Allows us to add edges between nodes
    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex) # Source vertex is the vertex that calls the function, that's why we pass self
        self.neighbors.append(edge) # Make sure the source vertex knows about this new edge


class Dijikstra:
    def __init__(self):
        # Create a minimum heap to store the nodes, since this is much more efficient implementation
        # than using an adjacency list, cost table, etc.
        self.heap =[]

    def calculate_distance(self, start_vertex):
        start_vertex.min_distance = 0 # Because the distance between the starting vertex and itself is... 0
        heapq.heappush(self.heap, start_vertex) # Push the start vertex to the heap.  It will be the lowest cost node at first
        # Begin working our way through the heap to find the shortest path
        while self.heap:

            if current_vertex.visited == True:
                continue # Skips to the next unvisited node if we encountered a visited one
            # Extract the lowest cost node from the heap, since this is a minimum heap, we need to pop the 
            # first element.  This will be the starting node at first
            current_vertex = heapq.heappop(self.heap) 
            # Now, for the minimum cost node we've chosen, explore its edges
            for edge in current_vertex.neighbors:
                edge_start_vertex = edge.start_vertex # Current minimum node
                edge_end_vertex = edge.end_vertex # Node at which this edge terminates
                path_distance = edge_start_vertex.min_distance + edge.weight # The minimum path distance so far plus the distance to the termination node
                # If the path distance we just computed is less than the previously calculated distance to that end node, we must update it
                if path_distance < edge_end_vertex.min_distance:
                    edge_end_vertex.min_distance = path_distance
                    edge_end_vertex.predecessor = edge_start_vertex # Must update the predecessor too, since its quicker to get there from that node
                    # Update the heap by pushing the updated end vertex.  Note that this will result in
                    # duplicate vertices being present in the heap, but it doesn't really matter since
                    # they are 'inert' for our purposes.  We live with dupes rather update the heap object
                    # itself because updating would take O(N) time, and we want this process to be efficient
                    heapq.heappush(self.heap, edge_end_vertex) 
            current_vertex.visited = True # We've now fully explored the toplogy of the current node, so mark it as visited.


    # Prints the shortest path
    def get_shortest_path(self, vertex):
        print("Total Path Length: ", vertex.min_distance)
        current_vertex = vertex
        while current_vertex is not None: # Until we get to the beginning of the path
            print(current_vertex.name, end="-") # Print the current vertex
            current_vertex = current_vertex.predecessor # And set the current vertex to be that of its predecessor


