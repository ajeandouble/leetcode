from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ans = 0
        N = len(cost)
        for i in range(2, N):
            min_prev_step = min(cost[i - 2], cost[i - 1])
            ans += min_prev_step
            cost[i] += min_prev_step
        return min(cost[-2], cost[-1])


sol = Solution()

cost = [10, 15, 20]
ans = sol.minCostClimbingStairs(cost)
print(f"{cost} => {ans}")
assert ans == 15

cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
ans = sol.minCostClimbingStairs(cost)
print(f"{cost} => {ans}")
assert ans == 6
