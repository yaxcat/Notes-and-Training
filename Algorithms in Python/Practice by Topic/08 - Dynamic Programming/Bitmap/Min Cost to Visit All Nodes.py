from math import inf

def min_cost_to_visit_every_node(graph: list[list[int]]) -> int:
    n = len(graph) # Get the number of nodes
    # Generate the DP list. Its size will be the 2 raised by the number of nodes.
    # This is because such a value is large enough to track the visitation status
    # of every node in binary form. The X column represents the node, while the 
    # Y column represents the combination of visited neighbors.
    dp = [[0]*n for _ in range(2**n)]

    # Bitmask represents the visited set of nodes:
    # - Each bit corresponds to a node.
    # - If bit i is set (1), node i has been visited.
    # 
    # This approach replaces the need for a traditional `visited` list:
    # - Each combination of visited nodes is uniquely represented by a bitmask integer.
    # - Importantly, bitmasks encode **which nodes have been visited**, not the order
    #   in which they were visited.
    #
    # Because each (bitmask, node) pair represents a unique traversal "state",
    # we can memoize results to avoid recomputing subproblems.

    def work_graph(bitmask, curr_node):
        # Base case 1 - We have reached the end of the graph. There are no more
        # nodes to account for, so return 0 cost
        if bitmask == (1<<n)-1:
            return 0
        # If we have already computed the minimum cost for this (bitmask, current 
        # node) combination, return the stored value.
        if dp[bitmask][curr_node] != 0:
            return dp[bitmask][curr_node]
        
        ans = inf # Initialize answer as a very high value so we find the min cost
        # Loop over the current node's neighbors
        for i in range(len(graph[curr_node])):
            # Check if the neighbor has not yet been visited and the edge value
            # is not zero (meaning there is an edge)
            if (bitmask & 1 << i) == 0 and graph[curr_node][i] != 0:
                # Answer will be the minimum of either the current answer or the 
                # result of backtracking.  If we need to backtrack, we'll stay at
                # current node and reset our bitmask to account for where we currently
                # are and what we've visited previously.  We will also make sure
                # to add the cost of the current node.
                ans = min(
                    ans,
                    work_graph(bitmask | 1<<i, i) + graph[curr_node][i],
                    )
        dp[bitmask][curr_node] = ans
        return ans
    result = work_graph(1, 0)
    return result if result < inf else -1

if __name__ == "__main__":
    graph = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = min_cost_to_visit_every_node(graph)
    print(res)
