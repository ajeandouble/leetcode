from typing import List
from time import sleep


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        permutation = []

        def helper(curr):
            print(curr)
            if len(curr) == 1:
                permutation.append(curr[0])
                return
            if len(curr) == 0:
                return

            for i in range(1, N):
                helper(curr[i:])
                # helper(curr[:i])

        helper(nums)


nums = [1, 2, 3]
ans = Solution().permute(nums)
print(f"ans of {nums} => {ans}")
