class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        q = deque()
        dist = 0

        def addLevel(r,c):
            if(r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in visited or grid[r][c] == -1):
                return
            q.append((r,c))
            visited.add((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
       
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                addLevel(r-1,c)
                addLevel(r+1,c)
                addLevel(r,c-1)
                addLevel(r,c+1)
            dist += 1
        


        
        