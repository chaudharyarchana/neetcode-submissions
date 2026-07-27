class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
        
        minHeap = [(0,k)]
        minTimes = {}

        while minHeap:
            time_k_to_i, i = heapq.heappop(minHeap)

            if i in minTimes:
                continue

            minTimes[i] = time_k_to_i  # to reach at i it takes time_k_to_i time

            for nei, time_i_nei in graph[i]:
                if nei not in minTimes:
                    heapq.heappush(minHeap, (time_k_to_i + time_i_nei, nei)) # time k to nei

        if len(minTimes) != n:
            return -1

        return max(minTimes.values())
        