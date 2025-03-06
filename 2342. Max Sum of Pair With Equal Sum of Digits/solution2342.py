from typing import List
from collections import defaultdict


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans = 0

        def digitsum(n):
            i = 0
            while len(str(n)) > 1 and i < 2:
                print(n)
                curr_total = 0
                factor = 1
                for c in str(n):
                    curr_total += int(c) * factor
                    factor *= 10
                n = str(curr_total)
                print(f"curr_total == {curr_total}")
                i += 1
            return int(n)

        s = defaultdict(int)
        for n in nums:
            total = digitsum(n)
            if total in s:
                ans = max(ans, total)
            s[total] = max(s[total], n)
            print(s)
        return ans


sol = Solution()
nums = [18, 43, 36, 13, 7]
ans = sol.maximumSum(nums)
print(f"{nums} -> {ans}")
