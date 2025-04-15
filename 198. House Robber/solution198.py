from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = [0] + nums
        print(nums)
        N = len(nums)

        for i in range(2, N):
            nums[i] = max(nums[i - 1], nums[i - 2] + nums[i])

        print(nums)
        return max(nums)


s = Solution()
lst = [5, 2, 2, 5]
ans = s.rob(lst)
print(ans)  # 4
