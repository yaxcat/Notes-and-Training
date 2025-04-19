import sys
from typing import List
from collections import deque

def task_scheduling(tasks: List[str], requirements: List[List[str]]) -> List[str]:
    # Generate a dictionary to hold the count of incoming edges for each node in
    # the graph
    def get_indegree(tasks, requirements):
        # Count the number of upstream nodes for a given node
        indegree = {task:0 for task in tasks}
        for r in requirements:
            indegree[r[1]] += 1
        # Identify neighbors of a given node
        neighbors = {task:[] for task in tasks}
        for r in requirements:
            neighbors[r[0]].append(r[1])

        return indegree, neighbors

    # Utilize Khan's algorithm to perform topological sort
    def topo_sort(indegree, tasks, neighbors):
        result = []
        q = deque()
        for task in tasks:
            if indegree[task] == 0:
                q.append(task)
        while q:
            curr_node = q.popleft()
            result.append(curr_node)
            # Loop over the current node's neighbors and decrement
            # the indegree since we've popped one of the in-edges
            for neighbor in neighbors[curr_node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
        return result
    
    indegree, neighbors = get_indegree(tasks, requirements)
    return topo_sort(indegree, tasks, neighbors)

if __name__ == "__main__":
    tasks = input().split()
    requirements = [input().split() for _ in range(int(input()))]
    res = task_scheduling(tasks, requirements)
    if len(res) != len(tasks):
        print(f"output size {len(res)} does not match input size {len(tasks)}")
        sys.exit()
    indices = {task: i for i, task in enumerate(res)}
    for req in requirements:
        for task in req:
            if task not in indices:
                print(f"'{task}' is not in output")
                sys.exit()
        a, b = req
        if indices[a] >= indices[b]:
            print(f"'{a}' is not before '{b}'")
            sys.exit()
    print("ok")
