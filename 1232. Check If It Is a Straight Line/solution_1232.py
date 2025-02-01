import sys
from typing import List
import math

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if (coordinates[1][0] - coordinates[0][0]) == 0:
            factor = 0
        else:
            factor = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])
        offset = coordinates[0][1] - (coordinates[0][0] * factor)
        print(f'factor={factor}, offset={offset}')
        for c in coordinates:
            if factor * c[0] + offset != c[1]:
                return False

        return True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
print(Solution().checkStraightLine(coordinates=coordinates))

coordinates = [[2,4],[10,16],[6,10]]
print(Solution().checkStraightLine(coordinates=coordinates))

coordinates = [[0,1],[0,-100],[0,10]]
print(Solution().checkStraightLine(coordinates=coordinates))
