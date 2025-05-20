from typing import List, Tuple
from functools import cache
from itertools import permutations


def getRotations(cuboid):
    return list(set(permutations(cuboid, 3)))


isStackable = lambda a, b: b[0] <= a[0] and b[1] <= a[1] and b[2] <= a[2]


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:  # type: ignore
        N = len(cuboids)
        cuboids: List[Tuple] = [tuple(cub) for cub in cuboids]

        def dfs(prev_cub, visited=tuple()):
            max_height = 0
            for cub in cuboids:
                if cub in visited:
                    continue
                rotations = getRotations(cub)
                for rot in rotations:
                    print(prev_cub, rot, isStackable(prev_cub, rot))
                    if not isStackable(prev_cub, rot):
                        continue
                    max_height = max(max_height, rot[2] + dfs(rot, visited + (cub,)))
                    print(
                        f"rot={rot}, prev_cub={prev_cub}, max_height={max_height}, visited={visited}"
                    )
            print(max_height)
            return max_height

        return dfs((float("+inf"), float("+inf"), float("+inf")))


# assert isStackable((37, 53, 95), (20, 45, 1000)) == True
# assert isStackable((30, 35, 95), (34, 29, 1000)) == True
# assert isStackable((30, 35, 95), (36, 29, 1000)) == False

maxHeight = Solution().maxHeight
# assert maxHeight([[50, 45, 20], [95, 37, 53], [45, 23, 12]]) == 190
assert maxHeight([[38, 25, 45], [76, 35, 3]]) == 76
