from typing import List


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        N = len(piles)
        suffixes = [0] * N
        suffixes[-1] = piles[-1]
        for i in range(N - 2, -1, -1):
            suffixes[i] = suffixes[i + 1] + piles[i]
        memo = {}

        def dfs(i: int, m: int) -> int:
            if i >= N:
                return 0
            if (i, m) in memo:
                return memo[(i, m)]
            max_stones = 0
            for X in range(1, 2 * m + 1):
                if i + X > N:
                    break
                opponent_optimal_score = dfs(i + X, max(X, m))
                player_score = suffixes[i] - opponent_optimal_score
                max_stones = max(max_stones, player_score)
            memo[(i, m)] = max_stones
            return memo[(i, m)]

        return dfs(0, 1)


assert Solution().stoneGameII([2, 7, 9, 4, 4]) == 10
