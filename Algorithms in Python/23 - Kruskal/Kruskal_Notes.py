import Disjoint_Set as dst

# TC: O()
# SC: O()

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