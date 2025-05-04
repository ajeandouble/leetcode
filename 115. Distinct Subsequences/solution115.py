class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        ROWS, COLS = len(s) + 1, len(t) + 1
        dp = [[0] * (COLS) for _ in range(ROWS)]

        for row in range(1, ROWS):
            for col in range(1, COLS):
                if s[row - 1] == t[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
        import numpy

        print(numpy.matrix(dp), end="\n")
        return dp[-1][-1]


assert Solution().numDistinct("rabbbit", "rabbit") == 3
