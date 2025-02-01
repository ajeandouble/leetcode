from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [0 for i in range(0, n+2)]
        dp[n] = 0
        if len(cost) == 2:
            return cost[0] if cost[0] < cost[1] else cost[1]
        for i in range(n-1, -1, -1):
            dp[i] = cost[i] + min(dp[i+2], dp[i+1])
            print(dp, f'\t\tcost[{i}]={cost[i]}')

        return min(dp[0], dp[1])

s = Solution()

# lst = [10, 15, 20]
# ans = s.minCostClimbingStairs(lst)
# print(f'{lst} -> {ans   }')

# lst = [1,100,1,1,1,100,1,1,100,1]
# ans = s.minCostClimbingStairs(lst)
# print(f'{lst} -> {ans   }')

lst = [1,100,1,1,1,100,1]
ans = s.minCostClimbingStairs(lst)
print(f'{lst} -> {ans   }')