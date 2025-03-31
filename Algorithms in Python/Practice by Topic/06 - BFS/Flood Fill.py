from typing import List
from collections import deque

# Performs functionality similar to the MS Paint bucket fill tool. Changes the value
# of a central node to some user specified one and then finds all contiguous cells 
# with that same value and changes those too.  Will run until no contiguous cells meeting
# the color requirement are found.
def flood_fill(
        r: int, 
        c: int, 
        replacement: int, 
        image: List[List[int]]
    ) -> List[List[int]]:

    num_rows = len(image)
    num_cols = len(image[0])
    def get_neighbors(coord, color): # Argument type is tuple
        y, x = coord
        # Clockwise, starting north
        delta_y = [-1, 0, 1, 0] 
        delta_x = [0, 1, 0, -1]
        # Find possible neighbors
        for val in range(len(delta_y)):
            ny = y+delta_y[val]
            nx = x+delta_x[val]
            # Check boundary before adding any neighbors
            if 0 <= ny < num_rows and 0 <= nx < num_cols:
                # We only want to return neighbors of the color that were
                # trying to change
                if image[ny][nx] == color:
                    # Using `yield` we can turn get_neighbors() into a
                    # generator, which remembers its state and will return
                    # the next neighbor each time we call it
                    yield ny, nx
    
    def bfs(root): # Argument type is tuple
        q = deque([root])
        # Since images/rasters are 2D objects, use a grid to track the nodes
        # we have visited
        visited = [[False for y in range(num_rows)] for x in range(num_cols)]
        y, x = root
        orig_color = image[y][x]
        image[y][x] = replacement # Replace the color at the root node
        visited[y][x] = True
        while len(q) > 0:
            # No need to track the level, can just pop the node and change
            # its neighbors' color
            curr_node = q.popleft()
            for neighbor in get_neighbors(curr_node, orig_color):
                ny, nx = neighbor
                if visited[ny][nx] == True:
                    continue
                image[ny][nx] = replacement
                visited[ny][nx] = True
                # Append the neighbor to the queue so that we can continue
                # applying the color change to neighbors of this neighbor
                # with that original color
                q.append(neighbor)

    bfs((r, c))
    return image

if __name__ == "__main__":
    r = 2
    c = 2
    replacement = 9
    image = [[0,1,3,4,1],[3,8,8,3,3],[6,7,8,8,3],[12,2,8,9,1],[12,3,1,3,2]]
    res = flood_fill(r, c, replacement, image)
    for row in res:
        print(" ".join(map(str, row)))
