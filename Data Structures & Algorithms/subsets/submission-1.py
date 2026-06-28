class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recursion(i, subsets):
            if i >= len(nums):
                res.append(subsets[:])
                return
            
            subsets.append(nums[i])
            recursion(i+1, subsets)
            subsets.pop()
            recursion(i+1, subsets)
        
        recursion(0,[])
        return res
        
             


        