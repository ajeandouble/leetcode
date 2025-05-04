from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        ROWS, COLS = len(dungeon), len(dungeon[0])
        dungeon[-1][-1] = 1 if dungeon[-1][-1] >= 0 else abs(dungeon[-1][-1]) + 1
        for col in range(COLS - 2, -1, -1):
            if dungeon[-1][col] - dungeon[-1][col + 1] >= 0:
                dungeon[-1][col] = 1
            else:
                dungeon[-1][col] = abs(dungeon[-1][col] - dungeon[-1][col + 1])

        for row in range(ROWS - 2, -1, -1):
            if dungeon[row][-1] - dungeon[row + 1][-1] >= 0:
                dungeon[row][-1] = 1
            else:
                dungeon[row][-1] = abs(dungeon[row][-1] - dungeon[row + 1][-1])

        for row in range(ROWS - 2, -1, -1):
            for col in range(COLS - 2, -1, -1):
                if (dungeon[row][col] - dungeon[row][col + 1] >= 0) or (
                    dungeon[row][col] - dungeon[row + 1][col] >= 0
                ):
                    dungeon[row][col] = 1
                else:
                    dungeon[row][col] = abs(dungeon[row][col] - min(dungeon[row][col + 1], dungeon[row + 1][col]))

        return dungeon[0][0]

assert Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]) == 7
assert Solution().calculateMinimumHP([[0]]) == 1
assert Solution().calculateMinimumHP([[0,0,0],[1,1,-1]]) == 1
assert Solution().calculateMinimumHP([[-3,5]]) == 4