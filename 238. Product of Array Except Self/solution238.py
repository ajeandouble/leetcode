from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ans = []
        prev = 1
        for n in nums:
            ans += [prev]
            prev *= n
        prev = 1
        for i in range(N - 1, -1, -1):
            ans[i] *= prev
            prev *= nums[i]
        return ans


sol = Solution()
nums = [1, 2, 3, 4]
ans = sol.productExceptSelf(nums)
print(f"{nums} => {ans}")
assert ans == [24, 12, 8, 6]

nums = [-1, 1, 0, -3, 3]
ans = sol.productExceptSelf(nums)
print(f"{nums} => {ans}")
assert ans == [0, 0, 9, 0, 0]
