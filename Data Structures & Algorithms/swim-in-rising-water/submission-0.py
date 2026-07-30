import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        visited = set()
        minHeap = [[grid[0][0],0,0]]
        ROWS,COLS = len(grid), len(grid[0])
        t = 0
        DIRECTIONS = [[-1,0],[1,0],[0,-1],[0,1]]


        while minHeap:
            t,r,c = heapq.heappop(minHeap)
            if r == ROWS - 1 and c == COLS - 1:
                return t

            for dr,dc in DIRECTIONS:
                neiR, neiC = r + dr, c + dc
                if (neiR >=0 and neiC >= 0 and neiR < ROWS and neiC < COLS and (neiR,neiC) not in visited):
                    visited.add((neiR,neiC))
                    heapq.heappush(minHeap,[max(t,grid[neiR][neiC]),neiR,neiC])
            
            

        