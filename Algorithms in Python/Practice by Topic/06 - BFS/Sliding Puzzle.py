from typing import List
from collections import deque

def num_steps(init_pos: List[List[int]]) -> int:
    # Board dimensions constrained by problem description
    num_rows = 2
    num_columns = 3

    # We must track the entire board configuration in visited in order to accurately
    # prune exploration later. Initialize to current configuration with 0 steps so far
    visited = {tuple(num for row in init_pos for num in row):0}
    goal = (1,2,3,4,5,0)

    # Identifies valid neighbors of the current node
    def get_neighbors(node):
        res = []
        # Stores the allowable movements on a flattened version of the 2D board
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        # Identify the position of the empty square and generate the board states as
        # we move tiles
        empty_pos = node.index(0)
        for neighbor in neighbors[empty_pos]:
            new_board = list(node[:])
            new_board[empty_pos], new_board[neighbor] = new_board[neighbor], new_board[empty_pos]
            res.append(tuple(new_board))
        return res
    
    # We're asked to find the quickest possible way to solve the puzzle, so use BFS to
    # build out the graph as we explore possibilities
    def bfs(root):
        flat = tuple(num for row in root for num in row)
        # Initial position could happen to be the solution
        if flat == goal:
            return 0
        # Initialize queue and the number of moves made
        q = deque([flat])
        # Loop over the queue
        while q:
            node = q.popleft()
            # Retrieve possible neighboring board states and add to the queue if 
            # they have not been visited
            for neighbor in get_neighbors(node):
                if neighbor in visited:
                    continue
                q.append(neighbor)
                visited[neighbor] = visited[node]+1
                if neighbor == goal:
                    return visited[neighbor]
        # If the case is unsolvable
        return -1
                
    num_moves = bfs(init_pos)

    return num_moves

if __name__ == "__main__":
    #init_pos = [[int(x) for x in input().split()] for _ in range(int(input()))]
    #print(init_pos)
    n = [[4, 1, 3], [2, 0, 5]]
    res = num_steps(n)
    print(res)
