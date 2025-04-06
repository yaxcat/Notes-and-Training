from typing import List
from math import inf
from collections import deque

INF = inf

def map_gate_distances(dungeon_map: List[List[int]]) -> List[List[int]]:
    num_rows = len(dungeon_map)
    num_cols = len(dungeon_map[0])
    visited = [[False for col in range(num_cols)] for row in range(num_rows)]
    
    # Performs an initial search on the grid, identifies gate locations and
    # adds those to the queue
    def find_gates(gate_val):
        gates = []
        for row in range(num_rows):
            for col in range(num_cols):
                if dungeon_map[row][col] == gate_val:
                    gates.append([row, col])
                    visited[row][col] = True
        return deque(gates)

    # Identifies valid neighbors using lists representing allowable XY alterations
    def get_neighbors(coord):
        y, x = coord
        res = []
        delta_y = [-1, 0, 1, 0]
        delta_x = [0, 1, 0, -1]
        for i in range(len(delta_y)):
            ny = delta_y[i] + y
            nx = delta_x[i] + x
            if 0 <= ny < num_rows and 0 <= nx < num_cols:
                if dungeon_map[ny][nx] == INF:
                    res.append([ny, nx])
        return res
    
    # Modified version of BFS which takes a queue representing all of the gates in
    # in the map. By starting with a queue initialized with all gates, we can compute
    # distances around the gates in parallel. Using the prequeued gates in tandem with
    # the visited list ensures that each navigable cell is encoded with the distance
    # from the closest gate, while simplifying the code
    def bfs(q):
        distance = 0
        while q:
            num_nodes = len(q)
            for _ in range(num_nodes):
                y, x = q.popleft()
                dungeon_map[y][x] = distance
                for ny, nx in get_neighbors([y, x]):
                    if visited[ny][nx]:
                        continue
                    q.append([ny, nx])
                    visited[ny][nx] = True
            distance += 1

    gates = find_gates(0)
    bfs(gates)
            
    return dungeon_map

if __name__ == "__main__":
    dungeon_map = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF],
    ]
    
    res = map_gate_distances(dungeon_map)
    for row in res:
        print(" ".join(map(str, row)))
