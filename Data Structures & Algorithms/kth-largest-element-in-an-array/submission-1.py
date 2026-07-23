class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = nums[:k]
        heapq.heapify(minHeap)

        for num in nums[k:]:
            if minHeap[0] < num:
                heapq.heapreplace(minHeap,num)
        return minHeap[0]
        