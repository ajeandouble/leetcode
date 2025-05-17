from typing import List
from functools import cache


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        sum_of_nums = sum(nums)
        if sum_of_nums % 2 != 0:
            return False

        @cache
        def dp(i, total) -> bool:
            if total == sum_of_nums / 2:
                return True
            if total > sum_of_nums / 2 or i >= N:
                return False
            if dp(i + 1, total + nums[i]) or dp(i + 1, total):
                return True
            return False

        return dp(0, 0)


assert Solution().canPartition([1, 5, 11, 5]) == True
assert Solution().canPartition([1, 2, 3, 5]) == False
assert Solution().canPartition([1, 5, 3]) == False
assert Solution().canPartition([2, 2, 1, 1]) == True
