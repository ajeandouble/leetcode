class Solution:
    def minDistance(self, text1: str, text2: str) -> int:
        N1, N2 = len(text1), len(text2)
        if N1 == 0 or N2 == 0:
            return max(N1, N2)
        dp = [[row] + [col + 1 for col in range(N2)] for row in range(N1 + 1)]
        for row in range(1, N1 + 1):
            for col in range(1, N2 + 1):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1]
                else:
                    replace = dp[row - 1][col - 1]
                    delete = dp[row][col - 1]
                    insert = dp[row - 1][col]
                    dp[row][col] = min(replace, delete, insert) + 1

        return dp[-1][-1]
    
assert Solution().minDistance("horse", "ros") == 3