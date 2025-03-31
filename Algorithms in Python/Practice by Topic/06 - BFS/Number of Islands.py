from typing import List
from collections import deque

def count_number_of_islands(grid: List[List[int]]) -> int:
    num_rows, num_cols = len(grid), len(grid[0])
    visted = [[False for c in range(num_cols)] for r in range(num_rows)] 
    
    def get_neighbors(node, ival):
        y, x = node
        # Starting north, moving clockwise
        y_delta = [-1,0,1,0]
        x_delta = [0,1,0,-1]
        for i in range(y_delta):
            ny = y+y_delta[i]
            nx = x+x_delta[i]
            # Make sure potential neighbor is within bounds
            if 0 <= ny < num_rows and 0 <= nx < num_cols:
                # Make sure the neighbor is an island
                if grid[y][x] == ival:
                    yield y,x
    def bfs(node):
        return
    
    return 0

if __name__ == "__main__":
    grid = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = count_number_of_islands(grid)
    print(res)
