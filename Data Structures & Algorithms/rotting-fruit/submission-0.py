class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        rotten = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    rotten.append((r,c))
        
        def addRotten(r,c):
            if(r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visited or grid[r][c] == 0 or grid[r][c] == 2):
                return
            grid[r][c] = 2
            visited.add((r,c))
            rotten.append((r,c))

        time = 0
        while rotten:
            for i in range(len(rotten)):
                r,c = rotten.popleft()
                addRotten(r+1,c)
                addRotten(r-1,c)
                addRotten(r,c+1)
                addRotten(r,c-1)
            if rotten : time += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1
        return time
        