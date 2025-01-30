from typing import List

def find_boundary(arr: List[bool]) -> int:
    if len(arr) == 0:
        return -1
    s = 0
    m = (len(arr)-1)//2
    e = len(arr)-1

    ind = -1
    while s <= e:
        if arr[m] == False:
            s = m+1
        else:
            ind = m
            e = m-1
        m = (s+e)//2
    return ind

if __name__ == "__main__":
    arr = [x == "true" for x in input().split()]
    res = find_boundary(arr)
    print(res)
