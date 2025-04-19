from typing import List
from collections import deque

def sequence_reconstruction(original: List[int], seqs: List[List[int]]) -> bool:
    # Construct a graph from the seqs
    def build_graph(seqs):
        # Construct the graph skeleton using unique nodes pulled from the subsequences
        unique_nodes = {node for seq in seqs for node in seq}
        graph = {node:[] for node in unique_nodes}

        # Loop over the individual subsequences
        for seq in seqs:
        # Each pair of adjacent elements (u, v) in a subsequence implies an edge u → v,
        # meaning u must come before v in the reconstructed sequence.
            for i in range(0, len(seq)-1):
                u, v = seq[i], seq[i+1]
                if v not in graph[u]:
                    graph[u].append(v)
        return graph
    
    # Build indegree map
    def get_indegree(graph):
        indegree = {node:0 for node in graph}
        # Loop over the graph and count the number of in edges for each neighbor node
        for node in graph:
            for neighbor in graph[node]:
                indegree[neighbor] += 1
        return indegree
    
    # Use Khan's algorithm to check for uniqueness
    def topo_sort(graph, indegree):
        # If a set of nodes from the graph is not identical to a set of nodes from
        # original, we can immediately return false
        if set(graph.keys()) != set(original):
            return False

        result = []
        q = deque()
        # Find any nodes without an in edge and add them to the queue since they
        # represent an entry point to the graph
        for node in indegree:
            if indegree[node] == 0:
                q.append(node)
        # Perform the topological sort on the graph, additionally check that the
        # length of the queue is at most 1 for any iteration
        while q:
            # Having more than one node in the queue at a time indicates the graph
            # is not linear. This means that it is possible to arrange the sequence
            # in more than one way, so we can abort early
            if len(q) > 1:
                return False
            curr_node = q.popleft()
            result.append(curr_node)
            # Decrement neighbor in edges by 1 to account for popping of upstream node
            for neighbor in graph[curr_node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return result
    
    graph = build_graph(seqs)
    indegree = get_indegree(graph)
    topo_result = topo_sort(graph, indegree)

    return topo_result == original

if __name__ == "__main__":
    original = [int(x) for x in input().split()]
    seqs = [[int(x) for x in input().split()] for _ in range(int(input()))]
    res = sequence_reconstruction(original, seqs)
    print("true" if res else "false")
