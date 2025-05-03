from heapq import heapify, heappop

def k_closest_points(points: list[list[int]], k: int) -> list[list[int]]:
    results = []
    # To ensure we account for negative coordinate values, calculate the distance squared from
    # the origin and set that value as the first element in each tuple.  Since heapify works in
    # element order, this ensures that all points are heaped by a valid distance measure
    dist_sqrd  = [(x**2+y**2, (x, y)) for (x, y) in points]
    print(dist_sqrd) # Illustrate the structure of dist_sqrd
    heapify(dist_sqrd)
    for _ in range(k):
        results.append(list(heappop(dist_sqrd)[1])) # Append only the point component to the results list
    return results

if __name__ == "__main__":
    points = [(1, 1), (2, 2), (3, 3)]
    k = 1
    res = k_closest_points(points, k)
    for row in res:
        print(" ".join(map(str, row)))
