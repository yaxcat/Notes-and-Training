# Implementation is much less messy if we just use a few classes

class Edge:
    def __init__(self, edge_weight, source_vertex, target_vertex):
        self.edge_weight = edge_weight
        self.source_vertex = source_vertex
        self.target_vertex = target_vertex

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False 
        self.predecessor = None
        self.neighbors = [] # Defines the topology around this node
        self.min_distance = float("inf") # Set to inifinity initially since we're trying to find the shortest path

    # Need to override the inbuilt function so that we can compare node distances
    def __lt__(self, other_node):
        return self.min_distance < other_node.min_distance
    
    # Allows us to add edges between nodes
    def add_edge(self, weight, destination_vertex):
        edge = Edge(weight, self, destination_vertex) # Source vertex is the vertex that calls the function, that's why we pass self
        self.neighbors.append(edge) # Make sure the source vertex knows about this new edge

