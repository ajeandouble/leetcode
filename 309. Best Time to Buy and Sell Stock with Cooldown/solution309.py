from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        dp = {}

        def dfs(i, buying=True):
            if i >= N:
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            # Hold
            hold_profit = dfs(i + 1, buying)
            if buying:
                # Max between buying vs holding - WHATEVER is optimal next
                buy_profit = -prices[i] + dfs(
                    i + 1, False
                )  # "you must sell the stock before you buy again"
                dp[(i, buying)] = max(buy_profit, hold_profit)
            else:
                # Max between selling and not being to sell on cooldown vs holding
                sell_profit = prices[i] + dfs(i + 2, True)
                dp[(i, buying)] = max(sell_profit, hold_profit)

            return dp[(i, buying)]

        return dfs(0, True)


assert Solution().maxProfit([1, 2, 3, 10]) == 9
assert Solution().maxProfit([0, 1, 2, 3, 42, 0, 39]) == 42
assert Solution().maxProfit([1, 2, 3, 0, 2]) == 3
assert Solution().maxProfit([1, 2, 4]) == 3
assert Solution().maxProfit([1]) == 0
assert Solution().maxProfit([42]) == 0
