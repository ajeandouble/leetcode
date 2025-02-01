from typing import List
from collections import defaultdict
import time


class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        maxPbyD = defaultdict(int)
        for i, d in enumerate(difficulty):
            p = profit[i]
            print(maxPbyD[d], p)
            maxPbyD[d] = max(maxPbyD[d], p)
        difficulty.sort()
        curr_max = 0
        for d in sorted(difficulty):
            maxPbyD[d] = max(curr_max, maxPbyD[d])
            curr_max = maxPbyD[d]

        ans = 0
        for w in worker:
            print(w)
            l, r = 0, len(difficulty) - 1
            found = False
            while l <= r and not found:
                mid = l + (r - l) // 2
                print(l, r, mid)
                if difficulty[mid] <= w and (
                    mid + 1 >= len(difficulty) or difficulty[mid + 1] > w
                ):
                    ans += maxPbyD[difficulty[mid]]
                    print(f"mid======={mid}, {difficulty[mid]} {ans}")
                    found = True
                elif difficulty[mid] <= w:
                    print(f"l={l}")
                    l = mid + 1
                    print(f"\tl={l}")
                else:
                    print(f"r={r}")
                    r = mid - 1
                    print(f"\tr={r}")
                time.sleep(0.1)
        return ans


# expected: 100
difficulty = [2, 4, 6, 8, 10]
profit = [10, 20, 30, 40, 50]
worker = [4, 5, 6, 7]

# expected: 190
difficulty = [13, 37, 58]
profit = [4, 90, 96]
worker = [34, 73, 45]

# expected : 324
difficulty = [68, 35, 52, 47, 86]
profit = [67, 17, 1, 81, 3]
worker = [92, 10, 85, 84, 82]

sol = Solution()
ans = sol.maxProfitAssignment(difficulty, profit, worker)
print(f"ans={ans}")
