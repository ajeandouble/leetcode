from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        N = len(digits)
        if N == 0:
            return
        ans = []
        comb = []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i):
            if i >= N:
                ans.append("".join(comb))
                return

            d = digits[i]
            for c in letters[d]:
                print(c)
                comb.append(c)
                print(comb)
                dfs(i + 1)
                comb.pop()

        dfs(0)
        return ans


sol = Solution()

digits = "23"
ans = sol.letterCombinations(digits)
print(f"{digits} => {ans}")
