from typing import List
from collections import deque

def count_number_of_islands(grid: List[List[int]]) -> int:
    num_rows, num_cols = len(grid), len(grid[0])
    visited = [[False for c in range(num_cols)] for r in range(num_rows)] 
    num_islands = 0

    def get_neighbors(node, ival):
        y, x = node
        # Starting north, moving clockwise
        y_delta = [-1,0,1,0]
        x_delta = [0,1,0,-1]
        for i in range(len(y_delta)):
            ny = y+y_delta[i]
            nx = x+x_delta[i]
            # Make sure potential neighbor is within bounds
            if 0 <= ny < num_rows and 0 <= nx < num_cols:
                # Make sure the neighbor is an island
                if grid[ny][nx] == ival:
                    yield ny,nx

    def bfs(root):
        q = deque([root])
        y, x = root
        visited[y][x] = True
        islands = []
        while len(q) > 0:
            island = []
            curr_node = q.popleft()
            for neighbor in get_neighbors(curr_node, 1):
                ny, nx = neighbor
                if visited[ny][nx] == True:
                    continue
                visited[ny][nx] = True
                num_cells += 1
                q.append(neighbor)
                island.append(neighbor)
            islands.append(island)
        return len(islands)

    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] != 0:
                num_islands += bfs([row, col])
    
    return num_islands

if __name__ == "__main__":
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = count_number_of_islands(grid)
    print(res)
