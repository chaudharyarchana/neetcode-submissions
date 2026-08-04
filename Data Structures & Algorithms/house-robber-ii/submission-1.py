class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0,0
        
        if len(nums) == 1:
            return nums[0]
            
        for num in nums[:-1]:
            temp = max(rob1+num,rob2)
            rob1 = rob2
            rob2 = temp
        
        rob3, rob4 = 0, 0

        for num in nums[1:]:
            temp = max(rob3+num,rob4)
            rob3 = rob4
            rob4 = temp
        
        return max(rob4,rob2)

        