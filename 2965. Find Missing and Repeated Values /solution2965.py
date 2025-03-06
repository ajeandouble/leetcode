from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        missing = 1
        repeated = None
        visited = set()
        for nums in grid:
            for n in nums:
                if n in visited:
                    repeated = n
                visited.add(n)
                while missing in visited and missing <= N**2:
                    missing += 1
        return [repeated, missing if missing not in visited else missing + 1]


sol = Solution()

input = [[1, 3], [2, 2]]
assert sol.findMissingAndRepeatedValues(input) == [2, 4]

input = [[1, 1], [3, 4]]
assert sol.findMissingAndRepeatedValues(input) == [1, 2]

input = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
assert sol.findMissingAndRepeatedValues(input) == [9, 5]

input = [[1, 3, 4], [9, 7, 5], [8, 2, 3]]
assert sol.findMissingAndRepeatedValues(input) == [3, 6]
