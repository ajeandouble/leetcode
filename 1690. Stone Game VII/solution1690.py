from typing import List
from itertools import accumulate


class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        N = len(stones)
        suffix_sum = list(accumulate(stones))[::-1] + [0]
        dp = [[None] * N for _ in range(N)]

        def dfs(l, r):
            if l >= r:
                return 0
            if dp[l][r] is not None:
                return dp[l][r]
            take_left = suffix_sum[l + 1] - suffix_sum[r + 1] - dfs(l + 1, r)
            take_right = suffix_sum[l] - suffix_sum[r] - dfs(l, r - 1)
            best_delta = max(take_left, take_right)
            dp[l][r] = best_delta
            return best_delta

        return dfs(0, N - 1)


assert Solution().stoneGameVII([7, 90, 5, 1, 100, 10, 10, 2]) == 122
assert Solution().stoneGameVII([5, 3, 1, 4, 2]) == 6
