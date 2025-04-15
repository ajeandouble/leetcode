from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        N = len(nums)
        ans = []
        curr = []

        def dfs(i):
            if i >= N:
                ans.append(curr.copy())
                return

            curr.append(nums[i])
            dfs(i + 1)
            curr.pop()
            while i + 1 < N and nums[i] == nums[i + 1]:
                i += 1
            dfs(i + 1)

        dfs(0)
        return ans


sol = Solution()
nums = [1, 2, 2]
ans = sol.subsetsWithDup(nums)
print(f"ans for {nums} => {ans}")
