from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('+inf')
        l, r = 0, 0
        curr = 0
        while l <= r and r < len(nums):
            curr += nums[r]
            while l <= r and curr >= target:
                curr -= nums[l]
                ans = min(ans, r - l + 1)
                l += 1
            r += 1
        return ans if ans != float('+inf') else 0

assert Solution().minSubArrayLen(7, [2,3,1,2,4,3]) == 2
assert Solution().minSubArrayLen(4, [1,4,4]) == 1
assert Solution().minSubArrayLen(11, [1,1,1,1,1,1,1,1]) == 0
assert Solution().minSubArrayLen(9, [4]) == 0
assert Solution().minSubArrayLen(9, [4,2]) == 0