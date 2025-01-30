# TC: O(V**3)
# SC: O(V**2)

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

# The key concept to understand how Floyd-Warshall can work for paths which connect more than two nodes is that the
# graph is modified with each iteration, which then informs the next iteration.  It is this self modification and 
# reference which allow us to find the most efficient route through multiple nodes.  Because the algorithm compares
# every node to every other node with each iteration and only cares about the distance metric, we can leverage the
# shortest path computed during the previous itration to find the best path to each destination node.  To see how
# this works, look at B -> D via C in the printout, diagram and excel sheet.
def floyd_warshall(num_vertices, graph):
    optimized = graph # Create a copy of the input graph so we can work on that instead of overwriting the original
    nodes = ['A', 'B', 'C', 'D']
    # Loop through all vertices
    for vertex in range(num_vertices):
        # Because FW works on a matrix, we must visit each vertex as though it were a cell in a 2D array/table
        print(f"Via: {nodes[vertex]}")
        for row in range(num_vertices): # as row
            for col in range(num_vertices): # as column
                # Now assess distance
                direct_distance = optimized[row][col]
                dist_source_to_intermediate = optimized[row][vertex]
                dist_intermediate_to_dest = optimized[vertex][col]
                print(f"--Direct: {nodes[row]} - {nodes[col]}: {direct_distance}")
                print(f"--S to I: {nodes[row]} - {nodes[vertex]}: {dist_source_to_intermediate}")
                print(f"--I to D: {nodes[vertex]} - {nodes[col]}: {dist_intermediate_to_dest}")
                optimized[row][col] = min(direct_distance, dist_source_to_intermediate + dist_intermediate_to_dest)
                print("")
        print("")
    print(num_vertices, optimized)


graph = [
    [0, 8, INF, 1],
    [INF, 0, 1, INF],
    [4, INF, 0, INF],
    [INF, 2, 9, 0]
]

floyd_warshall(4, graph)