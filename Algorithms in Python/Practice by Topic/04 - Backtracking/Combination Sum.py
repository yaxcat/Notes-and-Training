from typing import List

def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    combinations = []
    def dfs(nums, start, remaining, path):
        # If the remaining amount is zero, we have found a valid combination 
        # that sums up to the target. Append the combination to the results and return.
        if remaining == 0:
            combinations.append(path[:])
            return
        # Loop over the list of candidate numbers and explore their 
        # possible combinations
        for i in range(start, len(nums)):
            num = nums[i]
            # If the remaining amount minus the current number is less
            #  than zero, skip the current number since it cannot contribute 
            # to a valid combination
            if remaining - num < 0:
                continue
            # Start at i in the recursive call to allow reuse of the current 
            # candidate and avoid generating duplicate combinations in different 
            # orders
            dfs(nums, i, remaining-num, path+[num])
    candidates.sort() # Sorting the candidates ensures efficient pruning of invalid branches during the recursion.
    dfs(candidates, 0, target, [])
    return combinations

if __name__ == "__main__":
    txt = '2 3 6 7'
    candidates = [int(x) for x in txt.split()]
    target = 7
    res = combination_sum(candidates, target)
    for row in sorted(map(sorted, res)):
        print(" ".join(map(str, row)))
