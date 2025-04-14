from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        ans = []
        curr_subset = []

        def dfs(i: int):
            if i >= N:
                ans.append(curr_subset[::])
                return

            curr_subset.append(nums[i])
            dfs(i + 1)
            curr_subset.pop()
            dfs(i + 1)

        dfs(0)
        return ans


nums = [1, 2, 3]
ans = Solution().subsets(nums)
print(f"ans of {nums} => {ans}")
# assert ans == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
