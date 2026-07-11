class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board)
        col = len(board[0])
        visited = set()

        def backtrack(i,j,w):
            if w >= len(word):
                return True

            if (i < 0 or i >= row or j < 0 or  j >= col
             or (i,j) in visited 
             or (word[w] != board[i][j]) ):
                return False

            visited.add((i,j))

            if (backtrack(i-1,j,w+1) or  
                backtrack(i+1,j,w+1) or  
                backtrack(i, j-1, w+1) or  
                backtrack(i, j+1, w+1)):
               return True

            visited.remove((i,j))
                

        for i in range(row):
            for j in range(col):
                if backtrack(i,j,0):
                    return True
                    
        return False