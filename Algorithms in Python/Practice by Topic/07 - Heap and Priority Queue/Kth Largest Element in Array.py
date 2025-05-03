from heapq import heapify, heappop

# Finds the kth largest element in an unsorted list, where the
# elements within the list do not have to be unique
def find_kth_largest(nums: list[int], k: int) -> int:
    # Python implements a minimum heap by default, but we can
    # make it act like a maximum heap by multiplying keys by -1
    heap = [x*-1 for x in list(nums)]
    heapify(heap)
    # Loop over the heap and pop elements, return value at the
    # kth position, converting it back to the correct sign
    for _ in range(k):
        val = heappop(heap)
        if _ == k-1:
            return val*-1

if __name__ == "__main__":
    #nums = [int(x) for x in input().split()]
    nums = [3,2,1,5,6,4]
    k = 2
    res = find_kth_largest(nums, k)
    print(res)
