class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        island = 0

        def bfs(row,col):
            q = deque()
            q.append((row,col))

            while q:
                row,col = q.popleft()
                directions = [[0,-1], [0,1],[-1,0],[1,0]]

                for dr,dc in directions:
                    r,c = row + dr, col + dc
                    if (r >= 0 and r < rows and c >=0 and c < cols and grid[r][c] == "1" and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    island += 1
                    visited.add((r,c))
                    bfs(r,c)
        
        return island
        