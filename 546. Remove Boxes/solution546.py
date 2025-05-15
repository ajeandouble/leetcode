from typing import List
from functools import cache


class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        N = len(boxes)

        @cache
        def dp(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            print(f"dp {l}, {r}")
            max_score = 1 + dp(l + 1, r)
            duplicates = 1
            k = l + 1
            dps_total = 0
            while k <= r:
                if boxes[l] != boxes[k]:
                    i = 0
                    while k + i <= r and boxes[l] != boxes[k + i]:
                        print(
                            f"(boxes[{l}] == {boxes[l]}) != (boxes[{k + i}] == {boxes[k + i]})"
                        )
                        i += 1
                    dps_total += dp(k, k + i - 1)
                else:
                    i = 0
                    while k + i <= r and boxes[l] == boxes[k + i]:
                        i += 1
                        duplicates += 1
                max_score = max(
                    max_score,
                    dps_total + ((duplicates * duplicates) if duplicates > 1 else 0),
                )
                k += i

            print(f"max_score={max_score}")
            print(f"exit dp {l}, {r}")
            return max_score

        return dp(0, N - 1)


print(Solution().removeBoxes([1, 3, 1]))
assert Solution().removeBoxes([1, 1, 1]) == 9
assert Solution().removeBoxes([1, 1, 3, 1]) == 10
assert Solution().removeBoxes([1, 3, 2, 2, 2, 3, 4, 3, 1]) == 23
