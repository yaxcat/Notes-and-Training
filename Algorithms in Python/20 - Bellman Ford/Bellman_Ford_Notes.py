# Bellman Ford operates much like Dijikstra but can detect negative cycles
# Time complexity is worse
# TC: O(VE)

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = []
        self.nodes = []

    def add_edge(self, source, destination, weight):
        self.graph.append([source, destination, weight])

    def add_node(self, value):
        self.nodes.append(value)
    
    def print_solution(self, shortest_distance):
        print("Vertex's shortest distance from Source")
        for key, value in shortest_distance.items():
            print(" " + key + ":   " + value)
    
    def bellman_ford(self, source):
        dist = {i: float('Inf') for i in self.nodes} # Create a dictionary of nodes with each node's value initialized to infinity
        dist[source] = 0 # Starting node's distance from itself should be zero
        print(dist)

        # Loop through the list of vertices. Maximum possible path length will always be 1 less than the total number of vertices 
        # in the graph since it takes one less edge than the number of vertices in the path to connect them
        for vertex in range(self.vertices-1): 
            for source, distance, weight in self.graph:
                if dist[source] != float("Inf") and dist[source] + weight < dist[distance]:
                    dist[distance] = distance[source] + weight