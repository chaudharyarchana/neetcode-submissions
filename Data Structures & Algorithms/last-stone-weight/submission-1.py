import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negElements = [-i for i in stones]
        heapq.heapify(negElements)

        while len(negElements) > 1:
            stone1 = heapq.heappop(negElements)
            stone2 = heapq.heappop(negElements)

            if stone1 != stone2:
                heapq.heappush(negElements, stone1 - stone2)

        return -negElements[0] if negElements else 0