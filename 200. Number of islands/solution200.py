from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        st = []
        visited = set()
        m, n = len(grid), len(grid[0])
        for r in range(m):
            for c in range(n):
                if (r, c) in visited:
                    continue
                if grid[r][c] == "1":
                    ans += 1
                    st.append((r, c))
                    while len(st):
                        print(r, c, st)
                        r_, c_ = st.pop()
                        if (r_, c_) in visited:
                            continue
                        visited.add((r_, c_))
                        if c_ - 1 >= 0 and grid[r_][c_ - 1] == "1":
                            st.append((r_, c_ - 1))
                        visited.add((r_, c_))
                        if c_ + 1 < n and grid[r_][c_ + 1] == "1":
                            st.append((r_, c_ + 1))
                        if r_ - 1 >= 0 and grid[r_ - 1][c_] == "1":
                            st.append((r_ - 1, c_))
                        if r_ + 1 < m and grid[r_ + 1][c_] == "1":
                            st.append((r_ + 1, c_))
                else:
                    visited.add((r, c))
        return ans


s = Solution()
input = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

input = [["1", "1", "1"],
         ["0", "1", "0"],
         ["1", "1", "1"]]

ans = s.numIslands(input)
print(ans)
