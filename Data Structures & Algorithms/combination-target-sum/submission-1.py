class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def combinations(i, comb, curSum):
            if i >= len(nums) or curSum > target:
                return
            if curSum == target:
                res.append(comb[:])
                return
            combinations(i+1, comb, curSum)
            comb.append(nums[i])
            combinations(i, comb, curSum + nums[i])
            comb.pop()
            
        
        combinations(0,[],0)
        return res
        