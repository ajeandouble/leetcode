from typing import List


class Solution:
    def island_size(self, r, c, grid: List[List[int]], total=[0]) -> int:
        if (
            r < 0
            or r >= self.R
            or c < 0
            or c >= self.C
            or (r, c) in self.island_cell_area
            or grid[r][c] == 0
        ):
            return
        total[0] += 1
        self.island_cell_area[(r, c)] = total
        self.island_size(r - 1, c, grid, total)
        self.island_size(r, c + 1, grid, total)
        self.island_size(r + 1, c, grid, total)
        self.island_size(r, c - 1, grid, total)

    def check_islands_around(self, r, c, grid: List[List[int]]) -> int:
        if (r, c) in self.island_cell_area:
            return 0
        score = 0
        visited_islands = set()
        if (r - 1, c) in self.island_cell_area:
            neighbor_cell = self.island_cell_area[(r - 1, c)]
            score += neighbor_cell[0] if id(neighbor_cell) not in visited_islands else 0
            visited_islands.add(id(neighbor_cell))
        if (r, c + 1) in self.island_cell_area:
            neighbor_cell = self.island_cell_area[(r, c + 1)]
            score += neighbor_cell[0] if id(neighbor_cell) not in visited_islands else 0
            visited_islands.add(id(neighbor_cell))
        if (r + 1, c) in self.island_cell_area:
            neighbor_cell = self.island_cell_area[(r + 1, c)]
            score += neighbor_cell[0] if id(neighbor_cell) not in visited_islands else 0
            visited_islands.add(id(neighbor_cell))
        if (r, c - 1) in self.island_cell_area:
            neighbor_cell = self.island_cell_area[(r, c - 1)]
            score += neighbor_cell[0] if id(neighbor_cell) not in visited_islands else 0
            visited_islands.add(id(neighbor_cell))
        return score + 1

    def largestIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        self.R, self.C = len(grid), len(grid[0])
        self.island_cell_area = {}
        for r in range(self.R):
            for c in range(self.C):
                if (r, c) in self.island_cell_area or grid[r][c] == 0:
                    continue
                self.island_size(r, c, grid, [0])

        for r in range(self.R):
            for c in range(self.C):
                ans = max(ans, self.check_islands_around(r, c, grid))
        return ans if ans != 0 else self.R * self.C


sol = Solution()

input0 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1],
]
ans = sol.largestIsland(input0)
assert ans == 9

input1 = [
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
]
ans = sol.largestIsland(input1)
assert ans == 56

input2 = [
    [1, 1, 1, 0],
    [1, 1, 1, 1],
    [1, 1, 0, 0],
    [0, 0, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
]
ans = sol.largestIsland(input2)
assert ans == 15

input3 = [
    [1, 1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0],
    [0, 1, 1, 0, 0, 0],
]
ans = sol.largestIsland(input3)
assert ans == 10


input4 = [
    [1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [1, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 0, 1],
    [1, 1, 1, 0, 1, 1],
]
ans = sol.largestIsland(input4)
assert ans == 25
