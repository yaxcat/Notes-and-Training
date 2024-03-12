# Easier way to create a graph
from collections import defaultdict

class Graph:
    def __init__(self, num_vertices):
        self.graph = defaultdict(list)
        self.num_vertices = num_vertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    # Helper function to make things easier
    def topologicalSortUtility(self, vertex, visited, stack):
        visited.append(vertex) # Append the current vertex to our visited list
        for neighbor_vert in self.graph[vertex]: # Loop through the current node's neighbors
            if neighbor_vert not in visited:
                self.topologicalSortUtility(neighbor_vert, visited, stack) # Call the utility recursively, which gets us to the last dependent node in the graph
        stack.insert(0, vertex) # Finally, add the current vertex to the stack, whose FIFO structure combined with the recursive logic above will ensure the dependency structure is respected

    # TC: O(E + V) Since we're visiting all edges and nodes once
    # SC: O(E + V) Since we're creating two lists to store all the edges, and all the nodes
    def topologicalSort(self):
        visited = []
        stack = []

        for vertex in list(self.graph): # TODO understand this syntax
            if vertex not in visited:
                self.topologicalSortUtility(vertex, visited, stack)

        print(stack) # Verify the structure is correct


# my_graph = Graph(5)

my_graph = Graph(8)
my_graph.addEdge("A", "C")
my_graph.addEdge("C", "E")
my_graph.addEdge("E", "H")
my_graph.addEdge("E", "F")
my_graph.addEdge("F", "G")
my_graph.addEdge("B", "D")
my_graph.addEdge("B", "C")
my_graph.addEdge("D", "F")


#print(my_graph.graph)

my_graph.topologicalSort()