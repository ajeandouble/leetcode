from typing import List, Tuple


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if sum(candidates) < target:
            return []
        solutions = set()
        candidates = sorted(candidates)
        combinations = []
        visited_idxs = set()
        N = len(candidates)

        cur_sum = 0
        i = 0

        def bt(idx, curSum, curIdx, _d=0):
            if curSum == target:
                new_combs = [c for c in combinations]
                new_combs.sort()
                new_combs = tuple(new_combs)
                solutions.add(new_combs)
                return
            if len(visited_idxs) == len(candidates):
                return
            if curIdx >= N:
                return
            if curSum > target:
                return

            prev = -1
            for i in range(idx, N):
                # print(f"_d={_d} i={i}")
                if prev == candidates[i]:
                    continue
                if i in visited_idxs:
                    continue
                if curSum + candidates[i] > target:
                    return
                combinations.append(candidates[i])
                # print(f"i={i} _d={_d}, curSum={curSum + candidates[i]}, curIdx={curIdx} combinations={combinations}")
                visited_idxs.add(i)
                bt(idx + 1, curSum + candidates[i], i + 1, _d=_d + 1)
                visited_idxs.remove(i)
                combinations.pop()
                prev = candidates[i]

        bt(0, 0, 0)
        return [list(t) for t in solutions]


s = Solution()

candidates, target = [10, 1, 2, 7, 6, 1, 5], 8
ans = s.combinationSum2(candidates, target)
print(ans)

# candidates, target = [2,5,2,1,2], 5
# ans = s.combinationSum2(candidates, target)
# print(ans)

# candidates, target = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 27
# ans = s.combinationSum2(candidates, target)
# print(ans)

# candidates, target = [1,1,2], 4
# ans = s.combinationSum2(candidates, target)
# print(ans)

candidates, target = [1] * 100, 30
ans = s.combinationSum2(candidates, target)
print(ans)
