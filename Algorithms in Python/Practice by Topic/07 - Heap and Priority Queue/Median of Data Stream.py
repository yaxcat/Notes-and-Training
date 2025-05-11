from heapq import heappush, heappop

class MedianOfStream:
    # Use two heaps to optimize for time complexity;
    #             -
    # Ex: 1,2,3,4,5,6,7,8,9  median == 5
    #             -
    # Initialize heaps
    def __init__(self):
        # Note that heaps don't need to be sorted like the example because
        # all we need is the number(s) at the middle of the list.  The 
        # correspond to the first value in a min/max heap.
        self.smalls = [] # Holds the smaller half of the inputs; max heap
        self.bigs = [] # Holds the larger half of the inputs; min heap

    # Adds a number from the stream to the appropriate heap
    def add_number(self, num: float) -> None:
        # If the number is equal to or smaller than the largest value in the
        # low pile, put it there. Otherwise push to the big pile
        if len(self.smalls) == 0  or num <= -self.smalls[0]: # Revert the sign since its a max heap
            heappush(self.smalls, -num)
        else:
            heappush(self.bigs, num)

        # Difference between heap sizes must be at most 1, otherwise the tops
        # of the heaps will not point at the median
        if len(self.smalls) > len(self.bigs) + 1:
            heappush(self.bigs, -heappop(self.smalls))
        elif len(self.bigs) > len(self.smalls):
            heappush(self.smalls, -heappop(self.bigs))

    def get_median(self) -> float:
        median = None
        # If there is an odd number of entries, we can peek at the smalls heap
        # Because we push to it first, it is guaranteed to have the answer in
        # this case
        if len(self.smalls) > len(self.bigs):
            median  = -self.smalls[0]
        # If there is an even number of entries, we must average values from
        # each heap
        else:
            median = (self.smalls[0] + self.bigs[0]) / 2.0
        return median

if __name__ == "__main__":
    median_of_stream = MedianOfStream()
    n = int(input())
    for _ in range(n):
        line = input().strip()
        if line == "get":
            median = median_of_stream.get_median()
            print(f"{median:.1f}")
        else:
            num = float(line)
            median_of_stream.add_number(num)
