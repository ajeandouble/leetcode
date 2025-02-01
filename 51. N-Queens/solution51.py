import copy
from typing import List, Optional
import numpy

print_board = lambda x: print(numpy.matrix.view(numpy.array(x)))


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        vCols, vPosDiags, vNegDiags = set(), set(), set()

        board = [["."] * n for row in range(n)]
        # print(board)

        def bt(r):
            # print(r)
            if r == n:
                ans.append(["".join(row) for row in board])

            for c in range(n):
                if c in vCols or r + c in vPosDiags or r - c in vNegDiags:
                    continue
                vCols.add(c)
                vPosDiags.add(r + c) # (r, c)
                vNegDiags.add(r - c)
                board[r][c] = "Q"
                bt(r + 1)
                vCols.remove(c)
                print(r+c, r - c, (r + c) == (r - c))
                vPosDiags.remove(r + c)
                vNegDiags.remove(r - c)
                board[r][c] = "."

        cols, negDiags, posDiags = set(), set(), set()
        bt(0)
        return ans


s = Solution()

ans = s.solveNQueens(4)
print(ans)
