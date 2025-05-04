from typing import List
import numpy as np
from sys import stdout


class Solution:
    def maximalSquare(self, mat: List[List[str]]) -> int:
        ans = 0
        ROWS, COLS = len(mat), len(mat[0])
    
        for col in range(0, COLS):
            mat[0][col] = int(mat[0][col])
            if mat[0][col] == 1:
                ans = 1
        for row in range(1, ROWS):
            mat[row][0] = int(mat[row][0])
            if mat[row][0] == 1:
                ans = 1
     
        for i in range(1, 2):
            for row in range(1, ROWS):
                for col in range(1, COLS):
                    mat[row][col] = int(mat[row][col])
                    if mat[row][col] == 1:
                        ans = max(ans, 1)
                        min_square = min(
                            mat[row - 1][col - 1],
                            mat[row - 1][col],
                            mat[row][col - 1],
                        )
                        if min_square:
                            width = min_square + 1
                            mat[row][col] = width
                            ans = max(ans, width)
                        
        return ans * ans


s = Solution()

m = [
    ["1", "0", "1", "0", "0"],
    ["1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "0"],
]
assert s.maximalSquare(m) == 4

m = [["0", "1"], ["1", "0"]]
assert s.maximalSquare(m) == 1

m = [["0"]]
assert s.maximalSquare(m) == 0

m = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "1", "1", "0"],
    ["1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1"],
    ["0", "0", "1", "1", "1"],
]
assert s.maximalSquare(m) == 16

m = [
    ["0", "0", "0", "1"],
    ["1", "1", "0", "1"],
    ["1", "1", "1", "1"],
    ["0", "1", "1", "1"],
    ["0", "1", "1", "1"],
]
assert s.maximalSquare(m) == 9