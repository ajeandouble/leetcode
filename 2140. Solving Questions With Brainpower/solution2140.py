from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        N = len(questions)
        dp = [0] * N
        for i in range(N - 1, -1, -1):
            # value at [skip + 1] + current brainpower vs value at + 1
            points, skip = questions[i]
            if i + 1 >= N:
                dp[i] = points
            elif i + skip + 1 >= N:
                dp[i] = max(dp[i + 1], points)
            else:
                dp[i] = max(dp[i + 1], points + dp[i + skip + 1])

        return dp[0]


assert Solution().mostPoints([[3, 2], [4, 3], [4, 4], [2, 5]]) == 5
assert Solution().mostPoints([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]) == 7
