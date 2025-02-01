from typing import List


class Solution:
    def spiralMatrixIII(
        self, rows: int, cols: int, rStart: int, cStart: int
    ) -> List[List[int]]:
        visited = 0
        ans = []
        r, c = rStart, cStart
        while visited < rows * cols:
            ans += [r, c]
            v_r = r
            v_c = c
            while v_c < cols and visited < rows * cols:
                v_c += 1
                ans += [v_r, v_c]
