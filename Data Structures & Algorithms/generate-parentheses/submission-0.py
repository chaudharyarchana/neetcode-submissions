class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def recursion(openP, closeP, idx, currStr):
            if len(currStr) == n*2:
                ans.append(currStr)
                return

            if openP > 0:
                currStr += "("
                recursion(openP - 1, closeP, idx+1, currStr)
                currStr = currStr[:-1]

            if closeP > openP:
                currStr += ")"
                recursion(openP, closeP - 1, idx+1, currStr)

        recursion(n-1, n, 1, "(")
        return ans
        