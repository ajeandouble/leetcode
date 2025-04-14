from typing import List
from collections import defaultdict


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        return [
            n for _, n in sorted([(freq, n) for (n, freq) in d.items()], reverse=True)
        ][:k]


nums = [1, 1, 1, 2, 2, 3]
k = 2
ans = Solution().topKFrequent(nums, k)
print(f"{nums}, {k} => {ans}")
assert ans == [1, 2]
