# Bellman Ford operates much like Dijikstra but can detect negative cycles
# Time complexity is worse
# TC: O(VE)
# SC: O(V)

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.graph = [] # Holds the edges
        self.nodes = []

    def add_edge(self, source, destination, weight):
        self.graph.append([source, destination, weight])

    def add_node(self, value):
        self.nodes.append(value)
    
    def print_solution(self, shortest_distance):
        print("Vertex's shortest destination from Source")
        for key, value in shortest_distance.items():
            print(" " + key + ":   " + str(value))
    
    def bellman_ford(self, source):
        dist = {i: float('Inf') for i in self.nodes} # Create a dictionary of nodes with each node's value initialized to infinity
        dist[source] = 0 # Starting node's destination from itself should be zero
        print("")
        self.print_solution(dist)
        print("")
        # Loop through the list of vertices. Maximum possible path length will always be 1 less than the total number of vertices 
        # in the graph since it takes one less edge than the number of vertices in the path to connect them
        for i in range(self.vertices-1): # O(V)
            print("___________________________________________________________________________")
            print(i)
            # For each vertex, we must now loop through the entire list of potential edges.  By performing one loop through all
            # edges for every vertex in the graph, we ensure that there are enough iterations to find the shortest path. Note
            # defining the number of iterations needed by the number of nodes and edges (rather than some logical operator)
            # prevents the algorithm from falling into an inifite loop if a negative edge value exists in the graph.
            for source, destination, weight in self.graph: # O(E)
                print("---Source:", source)
                print("---Destination:", destination)
                print("---Weight", weight)
                print("------Starting dist[source]:", dist[source])
                # First check that source distance/weight is not equal to infinity. If it is, that means there is no known path to
                # that node yet and we must ignore it for the current iteration.  If the source distance is not infinity, we add the 
                # weight for that edge and check to see if it is less than the currently computed distance/weight associated with
                # that node. The iterative nature ensures that we will always update each node with the lowest cost path known in the
                # given step. Ultimately, this computes the shortest path distance. 
                if dist[source] != float("Inf") and dist[source] + weight < dist[destination]:
                    # Update the destination node with the new lowest cost
                    dist[destination] = dist[source] + weight
                    print(f"------ Distance to {destination} updated:", dist[destination])
                print("")
            print("")
        
        # Loop through the graph and determine if we have a negative cycle
        for source, destination, weight in self.graph:
            # The newly computed distance along the path should never be less than the existing path distance for a visited node. If it
            # is, notify the user that we have a negative cycle and quit.
            if dist[source] != float("Inf") and dist[source] + weight < dist[destination]:
                print("Graph contains a negative cycle")
                return
          
        self.print_solution(dist)


g = Graph(5)
g.add_node("A")
g.add_node("B")
g.add_node("C")
g.add_node("D")
g.add_node("E")
g.add_edge("A", "C", 6)
g.add_edge("A", "D", -6)
g.add_edge("B", "A", 3)
g.add_edge("C", "D", 1)
g.add_edge("D", "C", 2)
g.add_edge("D", "B", 1)
g.add_edge("E", "B", 4)
g.add_edge("E", "D", 2)
g.bellman_ford("E")