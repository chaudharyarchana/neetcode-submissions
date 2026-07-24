class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        ROWS, COLS = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, visited):
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if (
                    nr < 0 or nr >= ROWS or
                    nc < 0 or nc >= COLS or
                    (nr, nc) in visited or
                    heights[nr][nc] < heights[r][c]
                ):
                    continue

                dfs(nr, nc, visited)

        # Pacific (top row and left column)
        for c in range(COLS):
            dfs(0, c, pacific)

        for r in range(ROWS):
            dfs(r, 0, pacific)

        # Atlantic (bottom row and right column)
        for c in range(COLS):
            dfs(ROWS - 1, c, atlantic)

        for r in range(ROWS):
            dfs(r, COLS - 1, atlantic)

        ans = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pacific and (r, c) in atlantic:
                    ans.append([r, c])

        return ans