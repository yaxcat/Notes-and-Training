from typing import List

def feasible(newspapers_read_times, num_coworkers, limit):
    total_time = 0
    total_workers = 0
    for t in newspapers_read_times:
        if total_time + t > limit:
            total_time = 0
            total_workers += 1
        total_time += t
    # Edge case - if we have any time left after looping through
    if total_time != 0:
        total_workers += 1
    return total_workers <= num_coworkers

# The trick to this problem is to recognize that the newspapers_read_times
# list is not the list on which we need to perform binary search.  Instead
# we must use that list to create a range of times that might be feasible
# given the number of coworkers available and evaluate that range to find
# the answer.
def newspapers_split(newspapers_read_times, num_coworkers):
    s = max(newspapers_read_times) # Minimum possible time to read all papers is the highest read time in the list since we can't subdivide it further
    e = sum(newspapers_read_times) # Maximum possible time it would take is to have one person read all the papers

    # Now, search through our space of possible times using binary search
    best_time = -1
    while s <= e:
        m = (s+e)//2
        if feasible(newspapers_read_times, num_coworkers, m):
            best_time = m
            e = m-1
        else:
            s = m+1
    return best_time

if __name__ == "__main__":
    newspapers_read_times = [int(x) for x in input().split()]
    num_coworkers = int(input())
    res = newspapers_split(newspapers_read_times, num_coworkers)
    print(res)
