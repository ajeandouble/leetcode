from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        print(s)
        ans = 0
        for n in nums:
            if n - 1 not in s:
                curr_ans = 0
                while n + curr_ans in s:
                    s.remove(n + curr_ans)
                    curr_ans += 1
                ans = max(ans, curr_ans)
        return ans


sol = Solution()

nums = [100, 4, 200, 1, 3, 2]
ans = sol.longestConsecutive(nums)
print(f"{nums} -> {ans}")
assert ans == 4


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
ans = sol.longestConsecutive(nums)
print(f"{nums} -> {ans}")
assert ans == 9


nums = [1, 0, 1, 2]
ans = sol.longestConsecutive(nums)
print(f"{nums} -> {ans}")
assert ans == 3
