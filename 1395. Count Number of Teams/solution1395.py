from typing import List


class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        dp = [1] + [0] * (N - 1)
        dp2 = dp.copy()
        ans = 0
        for mid in range(1, N):
            left_lesser = left_greater = 0
            right_lesser = right_greater = 0

            for i in range(mid):
                if rating[i] < rating[mid]:
                    left_greater += 1
                elif rating[i] > rating[mid]:
                    left_lesser += 1

            for i in range(mid + 1, N):
                if rating[mid] < rating[i]:
                    right_greater += 1
                if rating[mid] > rating[i]:
                    right_lesser += 1

            ans += left_greater * right_greater
            ans += left_lesser * right_lesser

        return ans


assert Solution().numTeams([2, 3, 4, 5, 6]) == 10
assert Solution().numTeams([2, 3, 4, 5, 6, 7, 8, 1, 9, 10, 11]) == 123
