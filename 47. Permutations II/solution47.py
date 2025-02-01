from typing import List
from collections import defaultdict


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)

        ans = []

        visited = defaultdict(int)
        for n in nums:
            visited[n] += 1

        def dfs(path):
            if len(path) == N:
                ans.append(path)
            for n in visited:
                print(path, visited)
                if visited[n] > 0:
                    visited[n] -= 1
                    dfs(path + [n])
                    visited[n] += 1

        dfs([])
        return ans


s = Solution()
nums = [1, 1, 2]
ans = s.permuteUnique(nums)
print(f"{nums} => {ans}")
