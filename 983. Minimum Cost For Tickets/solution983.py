from typing import List

from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        N, ans = len(days), 0
        if N == 1:
            return min(costs)
        dp = [0] * 366
        i = 0
        while i < N:
            d = days[i]
            step_back_1 = (dp[d - 1] if d - 1 > 0 else 0) + costs[0]
            step_back_7 = (dp[d - 7] if d - 7 > 0 else 0) + costs[1]
            step_back_30 = (dp[d- 30] if d - 30 > 0 else 0) + costs[2]
            dp[d] += min(step_back_1, step_back_7, step_back_30)
            j = d + 1
            while i + 1 < N and j < days[i + 1]:
                dp[j] = dp[d]
                j += 1
            i += 1
        return dp[d]
    
assert Solution().mincostTickets([1,4,6,7,8,20], [2,7,15]) == 11
assert Solution().mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]) == 17