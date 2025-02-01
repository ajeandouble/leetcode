from typing import List
from collections import defaultdict


class Solution:
    def isNStraightHand(self, h: List[int], groupSize: int) -> bool:
        h = sorted(h)
        z = 0
        i = 0
        while i < len(h):
            curr = 1
            flag = True
            j = i
            print('yo', i, flag, curr, groupSize)
            while flag and curr <= groupSize:
                k = j
                while k + 1 < len(h) and h[j] == h[k]:
                    k += 1
                if k + 1 < len(h) and h[k] - h[j] == 1:
                    curr += 1
                    j = k
            print(curr)
            i += 1
            z += 10
            # while i + 1



hand, groupSize = [1,1,2,2,3,4,5,6], 2
print(Solution().isNStraightHand(hand, groupSize))
