from typing import List

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        ans = 0
        for i in range(k):
            ans += happiness[i] - i if happiness[i] - i >= 0 else 0
        return ans

s = Solution()
s.maximumHappinessSum([12, 1, 42], 3)