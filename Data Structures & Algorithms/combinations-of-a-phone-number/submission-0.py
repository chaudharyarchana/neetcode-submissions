class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        ans = []
        phone = {
          "2": "abc",
          "3": "def",
          "4": "ghi",
          "5": "jkl",
          "6": "mno",
          "7": "pqrs",
          "8": "tuv",
          "9": "wxyz"
         }

        def backtrack(i, curr):
            if i >= len(digits):
                ans.append(curr[:])
                return

            for letter in phone[digits[i]]:
                backtrack(i+1, curr + letter)

        if len(digits) : backtrack(0, "")
        return ans
        