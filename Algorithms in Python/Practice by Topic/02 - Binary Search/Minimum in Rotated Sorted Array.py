from typing import List

def find_min_rotated(arr: List[int]) -> int:
    if len(arr) == 0:
        return -1    
    s = 0
    e = len(arr)
    boundary_ind = 0
    while s <= e:
        m = (s+e)//2
        if arr[m] <= arr[-1]:
            boundary_ind = m
            e = m-1
        else:
            s = m+1
    return boundary_ind

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    res = find_min_rotated(arr)
    print(res)
