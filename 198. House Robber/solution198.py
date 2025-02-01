from typing import List

# Recursive solution

# class Solution:
#     def rob(self, nums: List[int]) -> int:
#         ans = 0
#         memo = {}
#         def recursive(nums, i, total):
#             nonlocal ans
#             N = len(nums)
#             if i >= N:
#                 return
#             total += nums[i]
#             ans = max(ans, total)
#             recursive(nums, i+2, total)
#             recursive(nums, i+3, total)

#         recursive(nums, 0, 0)
#         recursive(nums, 1, 0)
#         return ans

class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        print(dp)
        for i in range(1, N):
            if dp[i] > dp[i-1] + nums[i]:
                dp[i+1] = dp[i]
            else:
                dp[i+1] = dp[i-1] + nums[i]
            print(dp)
        ans = [dp[-1]]
        for i in range(0, N-1:
            if dp[i] > dp[i-1] + nums[i]:
                dp[i+1] = dp[i]
            else:
                dp[i+1] = dp[i-1] + nums[i]
            print(dp)
        ans.append(dp[-1])

        return max(ans)

s = Solution()

lst = [1,3,2,1,1,4]
ans = s.rob(lst)
print(ans) # 4
