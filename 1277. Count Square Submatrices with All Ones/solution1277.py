from typing import List


class Solution:
    def countSquares(self, mat: List[List[int]]) -> int:
        ans = 0
        ROWS, COLS = len(mat), len(mat[0])

        for col in range(0, COLS):
            mat[0][col] = int(mat[0][col])
            if mat[0][col] == 1:
                ans += 1
        for row in range(1, ROWS):
            mat[row][0] = int(mat[row][0])
            if mat[row][0] == 1:
                ans += 1

        for i in range(1, 2):
            for row in range(1, ROWS):
                for col in range(1, COLS):
                    mat[row][col] = int(mat[row][col])
                    if mat[row][col] == 1:
                        ans += 1
                        min_square = min(
                            mat[row - 1][col - 1],
                            mat[row - 1][col],
                            mat[row][col - 1],
                        )
                        if min_square != 0:
                            width = min_square + 1
                            mat[row][col] = width
                            ans += width - 1

        return ans


matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
assert Solution().countSquares(matrix) == 15

matrix = [[1, 0, 1], [1, 1, 0], [1, 1, 0]]
assert Solution().countSquares(matrix) == 7

matrix = [[0, 1, 1, 1], [1, 1, 1, 1], [0, 1, 1, 1]]
assert Solution().countSquares(matrix) == 15

matrix = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
assert Solution().countSquares(matrix) == 20
