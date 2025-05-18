from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def dp(n, total):
            if total == target and n == 0:
                return 1
            if n == 0:
                return 0
            ans = 0
            for face in range(1, k + 1):
                ans += dp(n - 1, total + face)
            return ans % (10**9 + 7)

        return dp(n, 0)
