class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r,c):
            dir = [[-1,0],[1,0],[0,-1],[0,1]]
            for dr,dc in dir:
                row, col = dr+r, dc+c
                if row >= 0 and row < ROWS and col >= 0 and col < COLS and board[row][col] == 'O':
                    board[row][col] = '#'
                    dfs(row,col)

        # traverse top and bottom boundaries
        for r in [0, ROWS - 1]:
            for c in range(0, COLS):
                if board[r][c] == 'O':
                    board[r][c] = '#'
                    dfs(r,c)
        
        # traverse left and right skip corners(already included in above traversal)
        for r in range(1, ROWS-1):
            for c in [0, COLS-1]:
                if board[r][c] == 'O':
                    board[r][c] = '#'
                    dfs(r,c)

        for r in range(0,ROWS):
            for c in range(0, COLS):
                if board[r][c] == '#':
                    board[r][c] = 'O'
                elif board[r][c] == "O":
                    board[r][c] = "X"
        