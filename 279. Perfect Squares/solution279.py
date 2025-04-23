from math import sqrt
from math import inf


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]
        max_sqrt = int(sqrt(n))
        for i in range(2, max_sqrt + 1):
            square = i * i
            for j in range(square, n + 1):
                dp[j] = min(dp[j], dp[j - square] + 1)
        return dp[n]


ans = Solution().numSquares(1)
assert ans == 1  # 1
ans = Solution().numSquares(2)
assert ans == 2  # 1 + 1
ans = Solution().numSquares(3)
assert ans == 3  # 1 + 1 + 1
ans = Solution().numSquares(4)
assert ans == 1  # 4
ans = Solution().numSquares(12)
assert ans == 3  # 4 + 4 + 4
ans = Solution().numSquares(14)
assert ans == 3  # 1 + 1 + 4 + 4 + 4
