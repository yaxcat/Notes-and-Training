import heapq

def heap_top_3(arr: list[int]) -> list[int]:
    heapq.heapify(arr) # heapify modifies the list in place and does not create a new heap object
    result = []

    for i in range(3):
        result.append(heapq.heappop(arr))

    return result

if __name__ == "__main__":
    arr = [3, 1, 2, 10, 33, 100, 20]
    res = heap_top_3(arr)
    print(" ".join(map(str, res)))
