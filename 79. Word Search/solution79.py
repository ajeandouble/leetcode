from typing import List, Dict, Optional


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        N = len(word)

        path = set()

        def bt(r, c, i):
            if i == N:
                return True
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            if word[i] != board[r][c]:
                return False
            if (r, c) in path:
                return False
            path.add((r, c))
            ans = (
                (bt(r - 1, c, i + 1))
                or (bt(r, c + 1, i + 1))
                or (bt(r + 1, c, i + 1))
                or (bt(r, c - 1, i + 1))
            )
            path.remove((r, c))
            return ans

        for r in range(0, ROWS):
            for c in range(0, COLS):
                if board[r][c] != word[0]:
                    continue
                if bt(r, c, 0):
                    return True

        return False


s = Solution()

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
ans = s.exist(board, word)
print(f"{board}, {word} => {ans}")
assert ans == True

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCB"
ans = s.exist(board, word)
print(f"{board}, {word} => {ans}")
assert ans == False
