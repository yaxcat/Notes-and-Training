from typing import List

def find_first_occurrence(arr: List[int], target: int) -> int:
    if len(arr) == 0:
        return -1
    s = 0
    m = (len(arr)-1)//2
    e = len(arr)-1

    ind = -1
    while s <= e:
        if arr[m] ==  target:
            ind = m
        if arr[m] < target:
            s = m+1
        else:
            e = m-1
        m = (s+e)//2
    return ind

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = find_first_occurrence(arr, target)
    print(res)
