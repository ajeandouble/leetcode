from typing import List
from functools import cache


class Solution:
    def minHeightShelves(self, books: List[List[int]], width: int) -> int:
        N = len(books)

        @cache
        def dp(i):
            if i >= N:
                return 0
            min_height = float("+inf")
            max_height = float("-inf")
            total_t = 0
            for j in range(N - i):
                t, h = books[i + j]
                if total_t + t > width:
                    break
                total_t += t
                max_height = max(max_height, h)
                min_height = min(min_height, max_height + dp(i + j + 1))
            return min_height

        return dp(0)


assert Solution().minHeightShelves([[1, 1], [2, 3], [2, 3]], 4) == 4
assert (
    Solution().minHeightShelves(
        [[1, 1], [2, 3], [2, 3], [1, 1], [1, 1], [1, 1], [1, 2]], 4
    )
    == 6
)
