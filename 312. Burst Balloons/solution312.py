from typing import List
from functools import cache


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        N = len(nums)
        memo = {}

        @cache
        def dfs(l, r):
            if l > r:
                return 0
            if r - l == 1:
                return 0
            score_when_bursted_last = float("-inf")
            for burst_idx in range(l + 1, r):
                score_when_bursted_last = max(
                    score_when_bursted_last,
                    dfs(l, burst_idx)
                    + nums[l] * nums[burst_idx] * nums[r]
                    + dfs(burst_idx, r),
                )
            return score_when_bursted_last

        return dfs(0, N - 1)


assert Solution().maxCoins([3, 1, 5, 8]) == 167
assert Solution().maxCoins([1, 5]) == 10
