class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1 :
            firstStone = heapq.heappop(stones)
            secondStone = heapq.heappop(stones)

            if firstStone != secondStone :
                heapq.heappush(stones, firstStone - secondStone)

        return -stones[0] if stones else 0