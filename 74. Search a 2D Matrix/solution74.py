from bisect import bisect_left
from typing import List, Optional

class Solution:
    def searchMatrix(self, matrix: List[List[int]], t: int) -> bool:
        l, r = 0, len(matrix) -1
        which_row = -1
        while l <= r:
            mid = l +  ((r - l) // 2)
            if matrix[mid][0] <= t and matrix[mid][-1] >= t:
                i = bisect_left(matrix[mid], t)
                if i != len(matrix[mid]) and matrix[mid][i] == t:
                    return True
                else: return False
            if matrix[mid][-1] < t:
                l = mid + 1
            else:
                r = mid - 1

        return False

s = Solution()
assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 5) == True
assert s.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13) == False

print(bisect_left([0,1,2,3,4], -1))