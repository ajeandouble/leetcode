from typing import List, Optional, Dict
from collections import defaultdict
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        s = set()
        candidates = sorted(candidates)
        def dp(i, path, total_sum):
            if i >= N:
                return
            total_sum += candidates[i]
            if total_sum >= target:
                if total_sum == target:
                    # print(f"i={i}, total_sum={total_sum}, path={path}")
                    path = tuple(path)
                    s.add(path)
                return
            while i < N:
                # print(i)
                dp(i, path + [candidates[i]], total_sum)
                i += 1
        for i in range(0, N):
            dp(i, [candidates[i]], 0)
        # for d.valu
        return [list(elem) for elem in s]

candidates, target = [2,3,6,7], 7
s = Solution()
ans = s.combinationSum(candidates, target)
# print(ans)
assert ans == [[2,2,3],[7]]
