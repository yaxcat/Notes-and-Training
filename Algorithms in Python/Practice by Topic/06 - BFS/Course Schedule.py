from typing import List
from enum import Enum

# If we use DFS to perform topological sort, we need more nuance than the
# standard visited list will provide. This is because with recursive implementation
# the current node occupies an intermediate state in-between not visited and
# fully visited
class State(Enum):
    NOT_VISITED = 0
    VISITING = 1
    VISITED = 2

def is_valid_course_schedule(n: int, prerequisites: List[List[int]]) -> bool:
    # Construct a graph of courses using the prereqs
    def construct_graph(n, prerequisites):
        # Courses are guaranteed to be number from 0 to n-1 and there
        # may be courses with no prereqs (nodes with no edges) so 
        # initialize the dictionary using n
        graph = {i: [] for i in range(n)}
        for dest, src in prerequisites:
            graph[src].append(dest)
        return graph

    # Initialize visited list
    visited = [State.NOT_VISITED for _ in range(n)]

    # Perform DFS on the graph
    def dfs(start, graph, visited):
        # First node has been added to the call stack, so mark as visiting
        visited[start] = State.VISITING
        # Explore the current node's neighborhood
        for neighbor in graph[start]:
            # Fully visited nodes are safe and we can move on
            if visited[neighbor] == State.VISITED:
                continue
            # If we've been pointed back to a node we are currently visiting
            # (still in the call stack) we have found a cycle
            if visited[neighbor] == State.VISITING:
                return False

            # If exploration of any branch finds a cycle, return false immediately
            if not dfs(neighbor, graph, visited):
                return False
            
        # After all neighbors have been explored, we can safely mark the current
        # node as visited
        visited[start] = State.VISITED

        # No cycles were found during exploration, so return true
        return True

    graph = construct_graph(n, prerequisites)
    # Run DFS starting from every possible node since graph componenents are not
    # guaranteed to be connected and a cycle may exist in any 'island'
    return all(dfs(i, graph, visited) for i in range(n))

if __name__ == "__main__":
    n = int(input())
    prerequisites = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = is_valid_course_schedule(n, prerequisites)
    print("true" if res else "false")
