from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = [x for x in candidates if x <= target]
        candidates.sort()
        N = len(candidates)
        ans = []
        curr_comb: List[int] = []
        remaining = target

        def bt(start_idx):
            nonlocal remaining
            if remaining == 0:
                ans.append(curr_comb.copy())
            for i in range(start_idx, N):
                if candidates[i] > remaining:
                    break

                curr_comb.append(candidates[i])
                remaining -= candidates[i]
                bt(i)
                curr_comb.pop()
                remaining += candidates[i]

        bt(0)
        return ans
