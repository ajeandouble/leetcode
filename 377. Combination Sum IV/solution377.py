from typing import List
from collections import defaultdict


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)
        dp[0] = 1  # empty combination!
        for t in range(1, target + 1):
            for n in nums:
                dp[t] += dp[t - n]
        return dp[target]


combinationSum4 = Solution().combinationSum4
assert combinationSum4([1, 2, 3], 4) == 7
assert combinationSum4([42], 3) == 0
