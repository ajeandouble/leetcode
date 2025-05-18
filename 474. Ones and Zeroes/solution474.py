from typing import List
from functools import cache


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        N = len(strs)
        for i, s in enumerate(strs):
            t = [0, 0]
            for c in s:
                if c == "0":
                    t[0] += 1
                else:
                    t[1] += 1
            strs[i] = t  # type: ignore

        max_total = 0
        memo = {}

        @cache
        def dp(i, zeroes, ones, items):
            if i >= N:
                return 0
            curr_zeroes, curr_ones = strs[i][0], strs[i][1]
            dp_keep = float("-inf")
            if zeroes + curr_zeroes <= m and ones + curr_ones <= n:
                dp_keep = 1 + dp(
                    i + 1, zeroes + curr_zeroes, ones + curr_ones, items + 1
                )
            dp_skip = dp(i + 1, zeroes, ones, items + 1)
            return max(dp_keep, dp_skip)

        return dp(0, 0, 0, 0)  # type: ignore


findMaxForm = Solution().findMaxForm
assert findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4
assert findMaxForm(["10", "0001", "111001", "1", "0"], 1, 1) == 2
