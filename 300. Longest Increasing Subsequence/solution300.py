from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N
        ans = 1
        for r in range(1, N):
            curr_max = 1
            for l in range(0, r):
                if nums[l] < nums[r]:
                    curr_max = max(curr_max, dp[l] + 1)
            dp[r] = curr_max
            ans = max(ans, curr_max)
        return ans


assert Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
assert Solution().lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
assert Solution().lengthOfLIS([1, 2, 3, 4]) == 4
assert Solution().lengthOfLIS([4, 3, 2, 1]) == 1
