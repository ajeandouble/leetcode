from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS, COLS = len(dungeon), len(dungeon[0])
        dp = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        dp[-1][-1] = 1 if dungeon[-1][-1] >= 0 else abs(dungeon[-1][-1]) + 1
        for col in range(COLS - 2, -1, -1):
            if dungeon[-1][col] - dp[-1][col + 1] >= 0:
                dp[-1][col] = 1
            else:
                dp[-1][col] = abs(dungeon[-1][col] - dp[-1][col + 1])

        for row in range(ROWS - 2, -1, -1):
            if dungeon[row][-1] - dp[row + 1][-1] >= 0:
                dp[row][-1] = 1
            else:
                dp[row][-1] = abs(dungeon[row][-1] - dp[row + 1][-1])

        for row in range(ROWS - 2, -1, -1):
            for col in range(COLS - 2, -1, -1):
                if (dungeon[row][col] - dp[row][col + 1] >= 0) or (
                    dungeon[row][col] - dp[row + 1][col] >= 0
                ):
                    dp[row][col] = 1
                else:
                    dp[row][col] = abs(dungeon[row][col] - min(dp[row][col + 1], dp[row + 1][col]))

        return dp[0][0]
