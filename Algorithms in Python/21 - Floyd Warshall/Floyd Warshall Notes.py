# TC: O()
# SC: O()

# Implementation is easy

INF = 99999
# For printing the solution
def print_solutions(num_vertices, optimized):
    for i in range(num_vertices):
        for j in range(num_vertices):
            if optimized[i][j] == INF:
                print("INF", end=" ")
            else:
                print(optimized[i][j], end=" ")
        print(" ")


def floyd_warhsall(num_vertices, graph):
    optimized = graph # Create a copy of the input graph so we can work on that instead of overwriting the original

    # Loop through all vertices
    for vertex in range(num_vertices):
        # Because FW works on a matrix, we must visit each vertex as though it were a cell in a 2D array/table
        for row in range(num_vertices): # as row
            for col in range(num_vertices): # as column
                # Now assess distance
                direct_distance = optimized[row][col]
                dist_source_to_intermediate = optimized[row][vertex]
                dist_intermediate_to_dest = optimized[vertex][col]
                optimized[row][col] = min(direct_distance, dist_source_to_intermediate + dist_intermediate_to_dest)
    print(num_vertices, optimized)


    graph = [
        [0, 8, INF, 1],
        [INF, 0, 1, INF],
        [4, INF, 0, INF],
        [INF, 2, 9, 1]
    ]