class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visited = set()
        maxArea = 0

        def bfs(r,c):
            visited.add((r,c))
            area = 1
            directions = [[0,1],[0,-1],[1,0],[-1,0]]
            queue = deque()
            queue.append((r,c))

            while queue:
                row,col = queue.popleft()
                for dr,dc in directions:
                    r,c = dr + row, dc + col
                    if r>=0 and c>=0 and r < rows and c < cols and grid[r][c] == 1 and (r,c) not in visited:
                        queue.append((r,c))
                        visited.add((r,c))
                        area += 1
            return area


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    maxArea = max(maxArea, bfs(r,c))
        return maxArea