from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = nums
        print(nums)
        N = len(nums)

        ans = 0
        p = 0
        q = nums[0]
        for i in range(1, N):
            old_p = p
            p = q
            q = max(q, old_p + nums[i])
            ans = max(ans, q)
            print(p, q)

        return ans


s = Solution()
lst = [5, 2, 2, 5]
ans = s.rob(lst)
print(ans)  # 4
