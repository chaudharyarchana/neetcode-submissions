class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def recursion(idx):
            if idx == len(nums):
                ans.append(nums.copy())
                return
            
            for i in range(idx, len(nums)):
                [nums[idx], nums[i]] = [nums[i], nums[idx]]
                recursion(idx+1)
                [nums[idx], nums[i]] = [nums[i], nums[idx]]

        recursion(0)
        return ans
        