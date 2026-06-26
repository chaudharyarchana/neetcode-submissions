class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        poppedEle = 0

        while k > 0 :
          poppedEle = heapq.heappop(nums)
          k -= 1

        return -poppedEle   