from typing import List, Tuple


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        print(sorted(candidates))
        candidates = [x for x in candidates if x <= target]
        candidates.sort()

        N = len(candidates)
        ans = []

        def dfs(i, comb, total):
            if total == target:
                ans.append(comb.copy())
                return
            if total > target or i >= N:
                return
            # includes candidates[i]
            comb.append(candidates[i])
            dfs(i + 1, comb, total + candidates[i])
            comb.pop()
            # skip candidates[i] duplicates
            while i + 1 < N and candidates[i] == candidates[i + 1]:
                i += 1
            # excludes candidates[i]
            dfs(i + 1, comb, total)

        dfs(0, [], 0)
        return ans


s = Solution()

candidates, target = [1, 1, 2, 2, 2, 5], 8
ans = s.combinationSum2(candidates, target)
