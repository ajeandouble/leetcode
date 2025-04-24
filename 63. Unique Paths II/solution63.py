from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # print(numpy.matrix(obstacleGrid))
        ROWS, COLS = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid = [
            [float("+inf") if square == 1 else 1 for square in row]
            for row in obstacleGrid
        ]
        is_after_obstacle = False
        for col in range(COLS):
            if obstacleGrid[0][col] == float("+inf"):
                is_after_obstacle = True
            elif is_after_obstacle:
                obstacleGrid[0][col] = float("+inf")
        is_after_obstacle = False
        for row in range(ROWS):
            if obstacleGrid[row][0] == float("+inf"):
                is_after_obstacle = True
            elif is_after_obstacle:
                obstacleGrid[row][0] = float("+inf")
        # print(numpy.matrix(obstacleGrid))
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if obstacleGrid[row][col] == float("+inf"):
                    continue
                top_sq = obstacleGrid[row - 1][col]
                left_sq = obstacleGrid[row][col - 1]
                if top_sq == float("+inf") and left_sq == float("+inf"):
                    obstacleGrid[row][col] = float("+inf")
                else:
                    obstacleGrid[row][col] = (
                        top_sq if top_sq != float("+inf") else 0
                    ) + (left_sq if left_sq != float("+inf") else 0)
                    pass
        # print(numpy.matrix(obstacleGrid))
        ans = obstacleGrid[-1][-1] 
        return ans if ans != float("+inf") else 0

ans = Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
assert ans == 2
ans = Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 1], [0, 0, 0]])
assert ans == 1
ans = Solution().uniquePathsWithObstacles([[0,1],[0,0]])
assert ans == 1
ans = Solution().uniquePathsWithObstacles([[0,1],[1,0]])
assert ans == 0
ans = Solution().uniquePathsWithObstacles([[0,1],[1,0]])
assert ans == 0