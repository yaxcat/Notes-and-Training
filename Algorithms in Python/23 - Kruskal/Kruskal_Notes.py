import Disjoint_Set as dst

# TC: O(Elog(E)) due to the fact that we must sort the edges in ascending order first
# SC: O(V + E)

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
        self.nodes = []
        self.MST = [] # minimum spanning tree

    def addEdge(self, source, destination, weight):
        self.graph.append([source, destination, weight])

    def addNode(self, value):
        self.nodes.append(value)

    
    def printSolution(self, source, destination, weight):
        for source, destination, weight in self.MST:
            print("%s - %s: %s" % (source, destination, weight))


    def kruskal(self):
        i, edge = 0, 0
        ds = dst.DisjointSet(self.nodes) # Create a set for each node.  Parents are set to themselves and ranks to 0 by default.
        self.graph = sorted(self.graph, key=lambda item: item[2]) # We must sort the graph list in ascending order
        # Loop through the edges and extract the data we need
        while edge < self.V - 1:
            source, destination, weight = self.graph[i]
            i += 1
            # Now, for the source and destination vertices, find out which set they are a part of. As we union sets together we
            # will find that more and more source and destination vertices in the edges we visit are in the same set.  If they are,
            # they'll form a cycle, so we want to disregard them.  The set union operation is what allows us to avoid cylces and
            # why we must bother with doing operations on the verices (rather than just appending edges to the MST object).
            source_node = ds.find(source) 
            dest_node = ds.find(destination)
            # If the source and destination are not part of the same set, build out the tree and union them
            if source_node != dest_node:
                edge += 1
                self.MST.append([source, destination, weight])
                ds.union(source, destination)
        self.printSolution(source, destination, weight)


g = Graph(5)
g.addNode('A')
g.addNode('B')
g.addNode('C')
g.addNode('D')
g.addNode('E')

g.addEdge('A', 'B', 5)
g.addEdge('A', 'C', 13)
g.addEdge('A', 'E', 15)
g.addEdge('B', 'A', 5)
g.addEdge('B', 'C', 10)
g.addEdge('B', 'D', 8)
g.addEdge('C', 'A', 13)
g.addEdge('C', 'B', 10)
g.addEdge('C', 'E', 20)
g.addEdge('C', 'D', 6)
g.addEdge('D', 'B', 8)
g.addEdge('D', 'C', 6)
g.addEdge('E', 'A', 15)
g.addEdge('E', 'C', 20)

g.kruskal()