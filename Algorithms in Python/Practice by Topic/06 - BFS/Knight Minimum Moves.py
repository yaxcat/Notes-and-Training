from collections import deque

def get_knight_shortest_path(x: int, y: int) -> int:
    
    # Retrieve neighbors using a knights movement topology in chess
    def get_neighbors(coord):
        res = []
        y, x = coord
        delta_y = [-2, -2, -1, 1, 2, 2, 1, -1]
        delta_x = [-1, 1, 2, 2, 1, -1, -2, -2]
        # Looping through the list of deltas and adding them to the
        # current position will yield the moves a knight is allowed
        # to make
        for i in range(len(delta_y)):
            ny = y+delta_y[i]
            nx = x+delta_x[i]
            # Since the plain is infinite, no need to check bounds,
            # just return all neighbors for the current node
            res.append((ny, nx))
        return res

    # Use BFS since we're trying to calculate the minimum number of
    # moves
    def bfs(root):
        q = deque([root])
        # We must use a set because the board is infinite
        visited = set()
        moves = 0
        while len(q) > 0:
            num_nodes = len(q)
            for _ in range(num_nodes):
                node = q.popleft()
                # If we've found the target, exit and return the moves
                if node == (y, x):
                    return moves
                # The graph is visually represented in a grid, but the number
                # of moves/levels actually corresponds to the topology of the
                # neighbors generated, which is not the same as a visual
                # grid in this case.
                for neighbor in get_neighbors(node):
                    if neighbor in visited:
                        continue
                    q.append(neighbor)
                    visited.add(neighbor)
            moves += 1 # Number of moves corresponds to the number of levels in the graph
        return moves # Kept for completeness. On an infinite board, we will always find the target and return early

    return bfs((0, 0)) # Knight starts out at 0,0

if __name__ == "__main__":
    x = int(input())
    y = int(input())
    res = get_knight_shortest_path(x, y)
    print(res)
