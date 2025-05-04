from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [float("+inf") for _ in range(amount)]
        for coin_val in coins:
            for val in range(coin_val, amount + 1):
                dp[val] = min(
                    dp[val],
                    coin_val // val if coin_val % val == 0 else float("+inf"),
                    1 + dp[val - coin_val],
                )
        return dp[-1] if dp[-1] != float("+inf") else -1


ans = Solution().coinChange([3, 7, 405, 436], 8839)
ans = Solution().coinChange([1,2,5], 3)
ans = Solution().coinChange([ 1, 9], 11)
ans = Solution().coinChange([10, 12, 1], 47)
