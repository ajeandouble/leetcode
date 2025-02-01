from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        candidates.sort()
        ans = []
        unique_paths = set()

        def dp(path, total, c):
            if tuple(path) in unique_paths:
                return False
            total += c
            if total > target:
                unique_paths.add(tuple(path))
                return False
            elif total == target:
                unique_paths.add(tuple(path))
                ans.append([candidates[x] for x in path])
                return False
            for i, c in enumerate(candidates):
                if not dp(path + [i], total, c):
                    break
            return True

        for i, c in enumerate(candidates):
            if c > target:
                break
            dp([i], 0, c)

        return ans


s = Solution()
candidates, target = [2,3,6,7], 7
ans = s.combinationSum(candidates, target)
print(ans)
