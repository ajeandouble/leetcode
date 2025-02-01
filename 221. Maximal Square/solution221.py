from typing import List
import numpy as np
from sys import stdout

class Solution:
    def maximalSquare(self, m: List[List[str]]) -> int:
        ans = 0
        R, C = len(m), len(m[0])
        m.append([0] * C)
        for row in m:
            row.append(0)
        for r in range(1, R):
            for c in range(1, C):
                i = int(m[r][c])
                if i >= 1:
                    if int(m[r][c-1]) and int(m[r-1][c]) and int(m[r-1][c-1]):
                        i = min(int(m[r][c-1]), int(m[r-1][c]), int(m[r-1][c-1])) + 1
                        m[r+1][c+1] = i
                        ans = max(ans, i)
                    ans = max(ans, 1)

        return ans * ans


s = Solution()

m = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
assert s.maximalSquare(m) == 4

m = [["0","1"],["1","0"]]
assert s.maximalSquare(m) == 1

m = [["0"]]
assert s.maximalSquare(m) == 0

m = [["1","1","1","1","0"],["1","1","1","1","0"],["1","1","1","1","1"],["1","1","1","1","1"],["0","0","1","1","1"]]
assert s.maximalSquare(m) == 16

m = [["0","0","0","1"],["1","1","0","1"],["1","1","1","1"],["0","1","1","1"],["0","1","1","1"]]
assert s.maximalSquare(m) == 9