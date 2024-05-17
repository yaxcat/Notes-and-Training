# Prims Algorithm can use either an adjacency list or matrix.  We use the matrix
# here, but the list is cheaper in terms of time complexity
# TC: O(V**3) Due to the three loops.  Could be O(ElogV) if using a list
# SC: O(V)


import sys

class Graph:
    def __init__(self, vertex_num, edges, nodes):
        self.nodes = nodes
        self.edges = edges
        self.vertex_num = vertex_num # number of vertices in the graph
        self.MST = []

    def print_solution(self):
        print("Edge : Weight")
        for s, d, w in self.MST:
            print("%s -> %s: %s" % (s, d, w))

    def prim(self):
        # initialize the visited list
        visited = [0] * self.vertex_num 
        visited[0] = True

        edge_num = 0
        
        while edge_num < self.vertex_num-1:
            min = sys.maxsize # lazy way to set the initial minimum node value to infinity
            # Now loop through the vertices
            for vertex in range(self.vertex_num): # For each vertex
                print("Source Vertex: " + self.nodes[vertex])
                if visited[vertex]: # Recheck each visited node each time
                    print("---True")
                    for adjacent in range(self.vertex_num): # Search through adjacent vertices
                        print("------Adjacent Vertex: " + self.nodes[adjacent])
                        if ((not visited[adjacent]) and self.edges[vertex][adjacent]): # If the vertex hasn't been visited and it corresponds to an edge
                            if self.edges[vertex][adjacent] < min:
                                min = self.edges[vertex][adjacent]
                                s = vertex
                                d = adjacent
                else:
                    print("---False")
            self.MST.append([self.nodes[s], self.nodes[d], self.edges[s][d]])
            visited[d] = True # Make sure to change the destination node to true so we can check it more in future itertations
            edge_num += 1
            print('\n\n')
        self.print_solution()

edges = [
        [0,10,20,0,0],
        [10,0,30,5,0],
        [20,30,0,15,6],
        [0,5,15,0,8],
        [0,0,6,8,0]
    ]

nodes = ['A','B','C','D','E']
g = Graph(5, edges, nodes)
g.prim()