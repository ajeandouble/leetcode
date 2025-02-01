from typing import List, Dict, Optional


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        W, H = len(board[0]), len(board)
        N = len(word)  # FIXME: useful?
        self.ans = False

        def bt(r, c, cur, visited):
            if (r < 0 or r >= H) or (c < 0 or c >= W):
                return
            if visited.count((r, c)):
                return
            print(cur, visited, r, c)
            cur += board[r][c]
            if cur == word:
                self.ans = True
                return
            visited.append((r, c))
            bt(r - 1, c, cur, visited)
            bt(r, c + 1, cur, visited)
            bt(r + 1, c, cur, visited)
            bt(r, c - 1, cur, visited)
            visited.pop()

        visited = []
        for r in range(0, H):
            for c in range(0, W):
                if board[r][c] not in word:
                    visited.append((r, c))

        for r in range(0, H):
            for c in range(0, W):
                if board[r][c] != word[0]:
                    continue
                bt(r, c, "", visited)

        return self.ans


s = Solution()

board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
ans = s.exist(board, word)
print(ans)
