from typing import List
import numpy


class Solution:
    def uniquePathsWithObstacles(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        is_starting_square_obstacle = grid[0][0] == 1
        grid[0][0] = int(not is_starting_square_obstacle)
        flag = is_starting_square_obstacle
        for col in range(1, COLS):
            if grid[0][col] == 1:
                flag = True
            grid[0][col] = 1 if grid[0][col] == 0 and not flag else 0
        flag = is_starting_square_obstacle
        for row in range(1, ROWS):
            if grid[row][0] == 1:
                flag = True
            grid[row][0] = 1 if grid[row][0] == 0 and not flag else 0

        for row in range(1, ROWS):
            for col in range(1, COLS):
                grid[row][col] = (
                    grid[row - 1][col] + grid[row][col - 1] if grid[row][col] == 0 else 0
                )
        return grid[-1][-1]


ans = Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
assert ans == 2
ans = Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 1], [0, 0, 0]])
assert ans == 1
ans = Solution().uniquePathsWithObstacles([[0, 1], [0, 0]])
assert ans == 1
ans = Solution().uniquePathsWithObstacles([[0, 1], [1, 0]])
assert ans == 0
ans = Solution().uniquePathsWithObstacles([[0, 1], [1, 0]])
assert ans == 0
ans = Solution().uniquePathsWithObstacles(
    [
        [
            0,
            0,
            0,
            0,
        ]
    ]
)
assert ans == 1
ans = Solution().uniquePathsWithObstacles([[1, 0, 1, 0, 1]])
assert ans == 0
ans = Solution().uniquePathsWithObstacles([[1]])
assert ans == 0
ans = Solution().uniquePathsWithObstacles([[1, 0]])
assert ans == 0
ans = Solution().uniquePathsWithObstacles([[0, 0]])
assert ans == 1
ans = Solution().uniquePathsWithObstacles([[0, 0, 0, 0]])
assert ans == 1
ans = Solution().uniquePathsWithObstacles([[0, 0, 0, 0, 1]])
assert ans == 0
