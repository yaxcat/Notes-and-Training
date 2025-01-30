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

from collections import deque

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

    # Adds an edge between two vertices if they both exist in the graph    
    def addEdge(self, vertex1, vertex2):
        # Check to make sure the vertices are in the graph
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            # Establish the edge by adding vertices to the appropriate places in the adjacency list
            self.adj_list[vertex1].append(vertex2)
            self.adj_list[vertex2].append(vertex1)
            return f"Vertex added between {vertex1} and {vertex2}"
        else:
            return "Could not add edge since one or more nodes is missing from graph"
        
    # Removes an edge from the graph
    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.adj_list.keys() and vertex2 in self.adj_list.keys():
            # Try to call the list's remove method on the appropriate vertex.  Both nodes may be in the graph but not actually have an
            # edge.  This would throw an error so we use try/accept.
            try:
                self.adj_list[vertex1].remove(vertex2)
                self.adj_list[vertex2].remove(vertex1)
                return f"Edge between {vertex1} and {vertex2} successfully removed"
            except ValueError: # If the node is present in the graph but not the particular section of the adj_list
                return f"{vertex1} and {vertex2} present, but there is not a symetrical edge between them to remove"
        else:
            return "Failed to remove edge, one or nodes is missing"
        
    # Remove a vertex from the graph
    # The strategy is to identify the vertex that needs to go and use its list of edges to remove the vertex we want to get rid of from
    # its neighbor nodes' lists.  That way, we don't have a bunch of dead/non-functional edges left over.  After this step, we delete the
    # node itself.
    def removeVertex(self, vertex_to_delete):
        if vertex_to_delete in self.adj_list.keys():
            # Find the vertex we wish to delete and loop through its list of neighbors/edges
            for neighbor_vertex in self.adj_list[vertex_to_delete]:
                self.adj_list[neighbor_vertex].remove(vertex_to_delete) # For each neighbor/edge delete the target vertex from the neighbor vertex's edge list
            del self.adj_list[vertex_to_delete] # Finally delete the target vertex itself
            return f"The target vertex {vertex_to_delete} has been deleted and its edges removed."
        return f"Unable to delete the target vertex {vertex_to_delete}"

    # Breadth first search
    # Starts at some arbitrary node and traverses the graph level by level.  It explores the starting node's
    # neighbors first, before descending to the next level.  See diagram.  Used if we know the target is
    # relatively close to the starting point
    # TC: O(V + E) Number of vertices + the number of edges.  Adding instead of multiplying because we're only visiting each node once
    # SC: O(V) Because we're adding vertices to the visited set
    def bfs(self, vertex):
        visited = set() # Keeps track of the nodes we've already been to. Using a set because performance is good for searches
        visited.add(vertex) # By default, we've visited the node we passed into the bfs function, so add it to the visited list
        queue = deque([vertex]) # A FIFO data structure will help us easily manage traversing through the graph. Creates a double ended queue which operates in O(1) time complexity
        while queue: # (While the queue is not empty)
            current_vertex = queue.popleft() # Remove the first element in queue
            print("Visited:", visited)
            print("Queue:", queue)
            print("Current Vertex:", current_vertex, "\n")
            for adjacent_vertex in self.adj_list[current_vertex]: # Now loop through the neighbor nodes of the current vertex
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    queue.append(adjacent_vertex) # Add the vertex to the queue so we can continue iterating through the graph

    
    # Depth first search
    # Starts at some arbitrary node and explores all along its deepest edge as far as it can before 
    # backtracking.  Goes deep into different levels of the graph first.  Used if we know the target is 
    # buried deep in the graph.
    # TC: O(V + E) Number of vertices + the number of edges.  Adding instead of multiplying because we're only visiting each node once
    # SC: O(V) Because we're adding vertices to the visited set               
    def dfs(self, vertex):
        visited = set()
        visited.add(vertex)
        stack = [vertex] # A LIFO structure is what we need here since it will naturally allow us to get the deepest edge
        while stack: 
            current_vertex = stack.pop() # Remove and return the last element from the stack
            print(current_vertex)
            # Now loop through the current vertex's neighbors and add them to the stack. By adding them
            # in this way and popping them the way we do, we ensure that traverse through the depth of
            # the deepest edge first
            for adjacent_vertex in self.adj_list[current_vertex]: 
                if adjacent_vertex not in visited:
                    visited.add(adjacent_vertex)
                    stack.append(adjacent_vertex)
    
    def printGraph(self):
        for vertex in self.adj_list:
            print(vertex, ":", self.adj_list[vertex])

    


my_graph = Graph()
print(my_graph.addVertex('a'))
print(my_graph.addVertex('b'))
print(my_graph.printGraph())
print(my_graph.addEdge('a', 'b'))
print(my_graph.printGraph())
print(my_graph.removeEdge('a', 'b'))
print(my_graph.printGraph())



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
print("\n\n\n\n\n")
my_new_graph = Graph(my_graph)
print("Breadth First Search:")
my_new_graph.bfs('a')
print("\n\nDepth First Search:")
my_new_graph.dfs('a')