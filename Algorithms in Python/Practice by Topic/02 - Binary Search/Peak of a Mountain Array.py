from typing import List

def peak_of_mountain_array(arr: List[int]) -> int:
    if len(arr) == 0:
        return -1
    s = 0
    e = len(arr)-1
    peak = -1
    while s <= e:
        m = (s+e)//2
        if m == len(arr)-1 or arr[m] > arr[m+1]:
            peak = m
            e = m-1
        else:
            s = m+1
    return peak
if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = peak_of_mountain_array(arr)
    print(res)
