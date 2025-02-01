from typing import List
import sys

import math

# recursive intuition

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        memo = {}
        for val in coins:
            memo[val] = 1
        stop = 0
        def solve(coins: List[int], amount: int) -> int:
            nonlocal stop # DEBUG: delete this
            if amount in memo:
                return memo[amount]
            coins_needed = math.pow(2,64)
            for val in coins:
                if amount-val >= 1:
                    coins_needed = min(coins_needed, solve(coins, amount-val) + 1)
                    memo[amount] = coins_needed
            return coins_needed

        ans = solve(coins, amount)
        return ans if ans != math.pow(2,64) else -1

# iterative final solution
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        if amount in coins:
            return 1
        memo = [float('inf')] * (amount + 1)
        coins_needed = float('inf')
        coins = sorted(coins, reverse=True)
        for val in coins:
            memo[val] = 1
        for i in range(1, amount+1):
            for coin in coins:
                # print(memo[i])
                if i - coin >= 0:
                    coins_needed = min(memo[i], memo[i-coin]+1)
                    memo[i] = coins_needed
        return coins_needed if coins_needed != float('inf') else -1


s = Solution()
coins, amount = [1,2,3], 25
ans = s.coinChange(coins, amount)
print(ans)

coins, amount = [1,2,5], 11
ans = s.coinChange(coins, amount)
print(ans)