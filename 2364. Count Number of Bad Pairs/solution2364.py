from typing import List
from collections import defaultdict


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        N = len(nums)
        # j - i == nums[j] - nums [i] --> nums[i] - i == nums[j] - j
        pre_computed = [n - i for n, i in enumerate(nums)]
        print(f"pre_computed={pre_computed}")
        d = defaultdict(int)
        good_pairs = 0
        for n, j in enumerate(nums):
            diff = n - j
            if diff in d:
                good_pairs += d[diff]
            d[diff] += 1
        return N - good_pairs


sol = Solution()
input = [4, 1, 3, 3]
ans = sol.countBadPairs(input)
print(f"{input} -> {ans}")
