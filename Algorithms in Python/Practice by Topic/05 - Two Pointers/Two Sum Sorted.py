from typing import List

def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    left = 0
    right = len(arr)-1
    remainder = -1

    while arr[left] + arr[right] != target:
        if target - arr[right] <= 0:
            right -= 1
            remainder = target - arr[right]
        if remainder - arr[left] > 0:
            left += 1
        if remainder - arr[left] == 0:
            return [left, right]

if __name__ == "__main__":
    txt = '2 3 5 8 11 15'
    arr = [int(x) for x in txt.split()]
    target = 8
    res = two_sum_sorted(arr, target)
    print(" ".join(map(str, res)))
