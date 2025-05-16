from typing import List
from functools import cache


class Solution:
    def largestSumOfAverages(self, nums: List[int], k: int) -> float:
        N = len(nums)
        prefix = [0]
        for i, n in enumerate(nums):
            prefix.append(n + prefix[i])
        avg = lambda i, j: (prefix[j] - prefix[i]) / (j - i)

        @cache
        def dfs(i, k):
            if i == N and k == 0:
                return 0
            if i == N or k == 0:
                return float("-inf")
            max_avg = 0
            for j in range(i + 1, N + 1):
                max_avg = max(max_avg, avg(i, j) + dfs(j, k - 1))
            return max_avg

        return dfs(0, k)


assert Solution().largestSumOfAverages([9, 1, 2, 3, 9], 3) == 20
assert Solution().largestSumOfAverages([1, 2, 3, 4, 5, 6, 7], 4) == 20.5
