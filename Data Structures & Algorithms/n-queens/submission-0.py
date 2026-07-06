class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols = set()
        posDia = set()
        negDia = set()
        ans = []
        board = [["."]*n for i in range(n)]

        def backtrack(row):
            if row >= n:
                copy = ["".join(row) for row in board]
                ans.append(copy)
                return

            for col in range(n):
                if(col in cols or row-col in negDia or row+col in posDia):
                    continue
                cols.add(col)
                posDia.add(col+row)
                negDia.add(row-col)
                board[row][col] = "Q"

                backtrack(row+1)
                cols.remove(col)
                posDia.remove(col+row)
                negDia.remove(row-col)
                board[row][col] = "."

        backtrack(0)
        return ans


        