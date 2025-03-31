from typing import List
from collections import deque

def shortest_path(graph: List[List[int]], a: int, b: int) -> int:
    # Returns a list representing the input node's neighbors
    def get_neighbors(node: int):
        return graph[node]

    # BFS template
    def bfs(root: int, target: int):
        queue = deque([root]) # stores an integer value representing a node in the graph
        visited = {root} # stores an integer value repesenting nodes that have already been considered
        print(type(visited))
        level = 0
        while len(queue) > 0:
            n = len(queue)
            # Loop through the neighbors in the current level
            for _ in range(n):
                node = queue.popleft()
                # Test if we've found the target using the current node
                if node == target:
                    return level
                # Loop through the current node's neighbors returned by the helper function
                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue
                    queue.append(neighbor)
                    # Mark a neighbor as visited as soon as it is discovered to ensure that we only
                    # visit each node once.  If we marked as visited in the popping stage, we might
                    # add the same node to the queue more than once and duplicate work or cause
                    # infinite loops
                    visited.add(neighbor)
            level += 1
        return level

    return bfs(a, b)


if __name__ == "__main__":
    graph = [[1, 2], [0, 2, 3], [0, 1], [1]]
    a = int(0)
    b = int(3)
    res = shortest_path(graph, a, b)
    print(res)
