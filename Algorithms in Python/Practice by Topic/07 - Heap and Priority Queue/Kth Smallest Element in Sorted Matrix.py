from heapq import heappop, heappush

def kth_smallest(matrix: list[list[int]], k: int) -> int:
    heap = []
    # Initialize the heap by looping over the matrix row-wise
    for row in matrix:
        heappush(heap, (row[0], row, 0))
    # Initialize the count of items popped from priority queue
    pq_count = 0
    val = None
    while pq_count < k:
        val, row, pointer = heappop(heap)
        #Enqueue the row-wise next smallest item for the current popped element
        if pointer+1 < len(row): # Make sure pointer is within bounds of the sublist
            heappush(heap, (row[pointer+1], row, pointer+1))
        pq_count += 1
    return val

if __name__ == "__main__":
    #matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
    #k = int(input())

    matrix = [
                [ 1,  5,  9],
                [10, 11, 13],
                [12, 13, 15]
                ]
    k = 8

    res = kth_smallest(matrix, k)
    print(res)
