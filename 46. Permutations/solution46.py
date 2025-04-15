from typing import List
from time import sleep


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        visited = [False] * N
        ans = []

        curr = []

        def bt(l):
            if l == N:
                ans.append(curr.copy())
            for i in range(N):
                if not visited[i]:
                    curr.append(nums[i])
                    visited[i] = True
                    bt(l + 1)
                    visited[i] = False
                    curr.pop()

        bt(0)
        return ans


nums = [1, 2, 3]
ans = Solution().permute(nums)
print(f"ans of {nums} => {ans}")
