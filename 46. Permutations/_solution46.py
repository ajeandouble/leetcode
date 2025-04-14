from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        if N == 1:
            return [nums]
        ans = []
        used = [False] * 6

        def dfs(path):
            if len(path) == N:
                ans.append(path)
                print(ans)
            for i, n in enumerate(nums):
                if not used[i]:
                    used[i] = True
                    dfs(path + [n])
                    used[i] = False

        dfs([])
        return ans


s = Solution()
nums = [1, 2, 3]
ans = s.permute(nums)
print(f"ans of {nums} => {ans}")
