#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# Build Order

# Build Order
#You are given a list of projects and a list of dependencies (which is a list of pairs of projects, 
# where the second project is dependent on the first project). All of a project's dependencies must 
# be built before the project is. Find a build order that will allow the projects to be built. If 
# there is no valid build order, return an error.

# projects a,b,c,d,e,f
# dependencies: (a,d), (f,b), (b,d), (f,a), (d,c)

def createGraph(projects, dependencies):
    projectGraph = {}
    for project in projects:
        projectGraph[project] = []
    for pairs in dependencies:
        projectGraph[pairs[0]].extend(pairs[1])
    return projectGraph

project = ['a', 'b', 'c', 'd', 'e', 'f']
dependencies = [('a','d'), ('f','b'), ('b','d'), ('f','a'), ('d','c')]



def helper(vertex, visited, stack, pg):
    visited.add(vertex)
    for pre_req in pg[vertex]:
        if pre_req not in visited:
            helper(pre_req, visited, stack, pg)
    stack.insert(0, vertex)


def findBuildOrder(projects, dependencies):
    pg = createGraph(projects, dependencies)
    visited = set()
    stack = []

    for prj in pg:
        if prj not in visited:
            helper(prj, visited, stack, pg)
    return stack


res = findBuildOrder(project, dependencies)
print(res)

# TODO - Figure out how to detect if there is a cycle and exit effectively if there is

#project = ['a', 'b']
#dependencies = [('a', 'b'), ('b', 'a')]