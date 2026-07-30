class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False]*n
        distance = [10000000]*n
        res, edge = 0,0
        node = 0

        distance[0] = 0
        
        while edge < n:
            edge += 1
            res += distance[node]
            visited[node] = True

            for i in range(n):
                if visited[i]:
                    continue

                currDis = abs(points[i][0] - points[node][0]) + abs(points[i][1] - points[node][1])
                distance[i] = min(distance[i],currDis)
            
            minDis = 10000000
            nextNode = -1
            # next node
            for i in range(n):
                if not visited[i] and minDis > distance[i]:
                    nextNode = i
                    minDis = distance[i]
            node = nextNode
        
        return res
                    



        