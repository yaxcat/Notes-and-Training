from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    nums.sort()
    output = []
    def dfs(start, path):
        if start == len(nums):
            output.append(path)
            return
        dfs(start+1, path + [nums[start]])
        print( "+", path)
        dfs(start+1, path)
        print("-", path)
        
    dfs(0, [])
    return output

if __name__ == "__main__":
    txt = '1 2 3'
    nums = [int(x) for x in txt.split()]
    res = subsets(nums)
    for row in sorted(map(sorted, res)):
        print(" ".join(map(str, row)))
