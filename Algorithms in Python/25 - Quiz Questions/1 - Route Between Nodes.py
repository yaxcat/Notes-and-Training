#   Created by Elshad Karimov 
#   Copyright © 2021 AppMillers. All rights reserved.

class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
    
    def addEdge(self, vertex, edge):
        self.gdict[vertex].append(edge)
    
    # DFS
    def checkRoute(self, startNode, endNode):
        visited = set()
        stack = []

        visited.add(startNode)
        stack.append(startNode)

        while stack:
            current_node = stack.pop()
            print(current_node)
            print(stack)
            for neighbor in self.gdict[current_node]:
                if neighbor == endNode:
                    return True
                if neighbor not in visited:
                    visited.add(neighbor)
                    stack.append(neighbor)
        return False


customDict = { "a" : ["c","d", "b"],
            "b" : ["j"],
            "c" : ["g"],
            "d" : [],
            "e" : ["f", "a"],
            "f" : ["i"],
            "g" : ["d", "h"],
            "h" : [],
            "i" : [],
            "j" : []
               }
 
g = Graph(customDict)


print(g.checkRoute("a", "k"))