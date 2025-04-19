from typing import List
from collections import deque

def task_scheduling_2(tasks: List[str], times: List[int], requirements: List[List[str]]) -> int:
    # Generate the graph and indegree
    def get_indegree(tasks, times, requirements):
        # Graph
        graph = {task:[] for task in tasks}
        for r in requirements:
            graph[r[0]].append(r[1])
        # Indegree
        indegree = {task:0 for task in tasks}
        for r in requirements:
            indegree[r[1]] += 1
        # Start time - We need additional dictionaries to account for time constraints imposed by
        # the problem
        task_times = {}
        for i in range(0, len(tasks)):
            task_times[tasks[i]] = times[i]
        start_time = {task:0 for task in tasks}

        return graph, indegree, task_times, start_time
    
    def topo_sort(graph, indegree, start_time, task_times):
        q = deque()
        # Enqueue initial nodes
        for node in indegree:
            if indegree[node] == 0:
                q.append(node)
        while q:
            curr_node = q.popleft()
            # Loop through the neighbors and update their indegree and start time
            for neighbor in graph[curr_node]:
                indegree[neighbor] -= 1
                # Either keep the neighbor's current start time, or update it to the start time of the current
                # node plus its run time, whichever is larger.  This allows us to account for tasks of differing
                # duration, which can be performed in parallel
                start_time[neighbor] = max(start_time[neighbor], start_time[curr_node]+task_times[curr_node])
                if indegree[neighbor] == 0:
                    q.append(neighbor)     
        return

    graph, indegree, task_times, start_time = get_indegree(tasks, times, requirements)
    topo_sort(graph, indegree, start_time, task_times)
    if len(tasks) == 0:
        return 0
    return max(start_time[task] + task_times[task] for task in tasks)


if __name__ == "__main__":
    tasks = input().split()
    times = [int(x) for x in input().split()]
    requirements = [input().split() for _ in range(int(input()))]
    res = task_scheduling_2(tasks, times, requirements)
    print(res)
