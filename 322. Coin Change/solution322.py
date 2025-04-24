from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()  # NOTE: is it necessary?
        print(coins, amount)
        ROWS = len(coins)
        COLS = amount + 1
        dp = [[float("+inf") for _ in range(COLS)] for _ in range(ROWS)]
        val = coins[0]
        for c in range(1, COLS):
            dp[0][c] = c // val if c % val == 0 else float("+inf")
        # maybe optimization with better steps! :-)
        for r in range(1, ROWS):
            val = coins[r]
            for c in range(1, COLS):
                m = dp[r-1][c]
                n =  c // val if c % val == 0 else float("+inf")
                o = float("+inf")
                if c >= val:
                    o = min(dp[r-1][c], 1 + dp[r][c - val])  # Use this coin
                o = c // val + dp[r-1][c % val] if c % val else float("+inf")
                dp[r][c] = min(m, n, o)
                #     # coin is a multiple of the current coin value
                #     a
                #     # if not and we already a multiple of such value
                #     b
                #     # if it's not we can combine with other coin(s)
                #     c
                # )
                # print(c // val * val)
                # print(dp)
        print(dp)
        return dp[-1][-1] if dp[-1][-1] != float("+inf") else -1

ans = Solution().coinChange([3,7,405,436], 8839)
print(ans) # 20
# ans = Solution().coinChange([1,2,5], 3)
# print(ans, 'wtf')
# ans = Solution().coinChange([ 1, 9], 11)
# print("ans", ans)
# ans = Solution().coinChange([10, 12, 1], 47)
# print("ans", ans)
