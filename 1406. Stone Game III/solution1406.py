from typing import List


class Solution:
    def stoneGameIII(self, stones: List[int]) -> str:
        N = len(stones)
        memo = {}

        def dfs(l):
            if l >= N:
                return 0
            if l in memo:
                return memo[l]
            max_delta = float("-inf")
            for n_stones in range(3):
                take = sum(stones[l : l + n_stones + 1])
                delta = take - dfs(l + n_stones + 1)
                if delta >= max_delta:
                    max_delta = delta
            memo[l] = max_delta
            return memo[l]

        alice_delta = dfs(0)
        if alice_delta == 0:
            return "Tie"
        elif alice_delta < 0:
            return "Bob"
        else:
            return "Alice"
        return "Fuck"


assert Solution().stoneGameIII([1, 2, 3, 7]) == "Bob"
assert Solution().stoneGameIII([1, 2, 3, 6]) == "Tie"
assert Solution().stoneGameIII([1, 2, 3, -9]) == "Alice"
assert Solution().stoneGameIII([1, 2, 3, -9]) == "Alice"
assert Solution().stoneGameIII([-1, -2, -3]) == "Tie"
