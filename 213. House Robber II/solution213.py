from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = nums
        N = len(nums)
        if N <= 3:
            return max(nums)

        def helper(nums):
            ans = 0
            p = 0
            q = nums[0]
            for i in range(1, len(nums)):
                old_p = p
                p = q
                q = max(q, old_p + nums[i])
                ans = max(ans, q)
                print(p, q)

            return ans

        return max(helper(nums[:-1]), helper(nums[1:]))


nums = [2, 3, 2]
ans = Solution().rob(nums)
print(f"{nums} => {ans}")
assert ans == 3

nums = [1, 2, 3, 1]
ans = Solution().rob(nums)
print(f"{nums} => {ans}")
assert ans == 4

nums = [1, 2, 3]
ans = Solution().rob(nums)
print(f"{nums} => {ans}")
assert ans == 3

nums = [1, 2, 1, 1]
ans = Solution().rob(nums)
print(f"{nums} => {ans}")
assert ans == 3

nums = [1, 1]
ans = Solution().rob(nums)
print(f"{nums} => {ans}")
assert ans == 1

nums = [200, 3, 140, 20, 10]
ans = Solution().rob(nums)
print(f"{nums} => {ans}")
assert ans == 340

nums = [1, 3, 1, 3, 100]
ans = Solution().rob(nums)
print(f"{nums} => {ans}")
assert ans == 103

nums = [2, 7, 7, 7, 4]
ans = Solution().rob(nums)
print(f"{nums} => {ans}")
assert ans == 14

nums = [2, 7, 9, 3, 1]
ans = Solution().rob(nums)
print(f"{nums} => {ans}")
assert ans == 11

nums = [2, 1, 1, 2]
ans = Solution().rob(nums)
print(f"{nums} => {ans}")
assert ans == 3
