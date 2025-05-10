from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        N = len(nums)

        def helper(n):
            if n == 1:
                return
            nonlocal nums
            newNums = [None] * (n // 2)
            for i in range(n // 2):
                if i % 2 == 0:
                    newNums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    newNums[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = newNums
            helper(n // 2)

        helper(N)
        return nums[-1]


assert Solution().minMaxGame([1, 3, 5, 2, 4, 8, 2, 2]) == 1
assert Solution().minMaxGame([3]) == 3
assert Solution().minMaxGame([42]) == 42
assert Solution().minMaxGame([70, 38, 21, 22]) == 22
