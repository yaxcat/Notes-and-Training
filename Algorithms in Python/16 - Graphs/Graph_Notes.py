# GRAPH TERMINOLOGY
#   1) Vertices - nodes of the graph
#   2) Edge - line that connects pairs of vertices
#   3) Unweighted graph - a graph in which all edges have the same value
#   4) Weighted graph - a graph in which the values associated with edges differ
#   5) Undirected graph - a graph in which the edges do not have a direction associated with them
#   6) Directed graph - edges have a direction associated with them
#   7) Cyclic graph - a graph which contains at least one loop
#       - A collection of nodes and edges arranged such that they can be transited completely while traversing back to
#       - to the starting point
#   8) Acyclic graph - graph with no loops
#   9) Tree - a special case of a directed and acyclic graph



# GRAPH TYPES

#   1) Unweighted Undirected 
#   2) Unweighted Directed - Can be bidirectional or unidirectional
#   3) Positive Weighted Undirected - weights are positive numbers
#   4) Positive Weighted Directed
#   5) Negative Weighted Undirected - weights can be both positive and negative numbers
#   6) Negative Weighted Directed

# GRAPH REPRESENTATION

#   1) Adjacency Matrix - 2D array equal to the size of the nuumber of nodes **2.  Elements in the matrix indicate whether the pairs
#      of vertices share an edge or not (are adjacent).  See graphic.
#           - Used when the graph is complete or nearly complete (nodes are highly interconnected)
#   2) Adjacency List - collection of unordered lists which represent the topology of a graph.  Individual lists describe the 
#      set of neighbors at that given vertex
#           - Used when there is a small number of edges

# Creates the graph using a dictionary if provided, or creates an empty dictionary to represent the graph if nothing is passed
# in
class Graph:
    def __init__(self, adj_list=None):
        if adj_list is None:
            adj_list = {}
        self.adj_list = adj_list
    
    # Adds a brand new vertex to the graph
    def addVertex(self, vertex):
        # First check to see if the node already exists
        if vertex in self.adj_list.keys():
            return "This node is already in the graph"
        # If not, add the node
        else:
            self.adj_list[vertex] = []
            return "Node added to graph"

    def printGraph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])


my_graph = Graph()
print(my_graph.addVertex('a'))
print(my_graph.printGraph())
print(my_graph.addVertex('a'))


my_graph_old = {
    'a' : ['b', 'c'],
    'b' : ['a', 'd', 'e'],
    'c' : ['a', 'e'],
    'd' : ['b', 'e', 'f'],
    'e' : ['b', 'c', 'd', 'f'],
    'f' : ['d', 'e']
}

my_graph = {
    'a': ['b','c','d'],
    'b': ['a','e'],
    'c': ['a','d'],
    'd': ['a','c','e'],
    'e': ['b','d']
}