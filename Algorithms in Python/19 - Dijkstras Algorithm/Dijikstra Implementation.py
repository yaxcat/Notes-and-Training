# Implementation is much less messy if we just use a few classes

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
            current_vertex = heapq.heappop(self.heap) # Extract the lowest cost node from the heap, since this is a minimum heap, we need to pop the first element.  This will be the starting node at first
            # Now, for the vertex we're at, examine its neighbors to understand their cost/distance from the current node
            for edge in current_vertex.neighbors:
                edge_start_vertex = edge.start_vertex # The vertex our current node connects to via this edge
                edge_end_vertex = edge.end_vertex # The next vertex after that
                path_distance = edge_start_vertex.min_distance + edge.weight # The distance from the current vertex to the end of this edge (a three node span)
                # If the path distance is less than the currently calculated distance to that end node, we must update it
                if path_distance < edge_end_vertex.min_distance:
                    edge_end_vertex.min_distance = path_distance
                    edge_end_vertex.predecessor = edge_start_vertex # Must update the predecessor too, since its quicker to get there from that node
                    # Update the heap by pushing the updated end vertex.  Note that this will result in
                    # duplicate vertices being present in the heap, but it doesn't really matter since
                    # they are 'inert' for our purposes.  We live with dupes rather update the heap object
                    # itself because updating would take O(N) time, and we want this process to be efficient
                    heapq.heappush(self.heap, edge_end_vertex) 
            current_vertex.visited = True