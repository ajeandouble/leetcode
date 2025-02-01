from typing import List
from collections import defaultdict


class Solution:
    def isNStraightHand(self, h: List[int], groupSize: int) -> bool:
        h = sorted(h)
        d = {x: h.count(x) for x in set(h)}
        partitions = []
        s = sorted(list(set(h)))
        i = 0
        while i < len(s):
            part = [s[i]]
            curr = 1
            while i + 1 < len(s) and s[i + 1] - s[i] == 1:
                part.append(s[i + 1])
                curr += 1
                i += 1
            if curr >= groupSize:
                partitions.append(part)
            i += 1
        count = 0
        print(f"partitions={partitions}")
        for part in partitions:
            i = 0
            while i + 1< len(part):
                if d[part[i + 1]] - d[part[i]] > 1:
                    print(i)
                    return False
                i += 1
            print(f"part={part}")
            # offset = 0
            # while len(part) - (groupSize + offset) >= 0:
            #     min_val = min([d[x] for x in part[offset : offset + groupSize]])
            #     for i in range(offset, groupSize + offset):
            #         count += min_val
            #         d[part[i]] -= min_val
            #     print(d)
            #     offset += 1
        print(count, len(h))
        return True
        return count == len(h)

hand, groupSize = [1,1,2,2,3,4,5,6], 2
print(Solution().isNStraightHand(hand, groupSize))
