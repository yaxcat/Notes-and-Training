from typing import List

def first_not_smaller(arr: List[int], target: int) -> int:
    if len(arr) == 0:
        return -1
    s = 0
    m = (len(arr)-1)//2
    e = len(arr)-1

    ind = -1
    while s <= e:
        if arr[m] < target:
            s = m+1
        else:
            ind = m
            e = m-1
        m = (s+e)//2
    return ind

if __name__ == "__main__":
    arr = [int(x) for x in input().split()]
    target = int(input())
    res = first_not_smaller(arr, target)
    print(res)
