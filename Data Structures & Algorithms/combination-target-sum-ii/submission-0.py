class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def recursion(i, subset, curSum):
            if curSum == target:
                res.append(subset[:])
                return
            if i >= len(candidates) or curSum > target:
                return
          
            subset.append(candidates[i])
            recursion(i+1, subset, curSum + candidates[i])
            subset.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            recursion(i+1, subset, curSum)

        recursion(0,[],0)
        return res


        