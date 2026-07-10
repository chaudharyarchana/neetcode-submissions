class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(o,c,curr):
            if len(curr) == n *2:
                ans.append(curr[:])
            
            if o > c:
                return
            
            if o > 0:
                backtrack(o-1,c,curr+"(")
                

            if c > 0:
                backtrack(o,c-1,curr+")")
                
        backtrack(n-1,n,"(")
        return ans
        