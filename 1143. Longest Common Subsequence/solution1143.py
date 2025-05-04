class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        N1, N2 = len(text1), len(text2)
        dp = [[0] * (N2 + 1) for _ in range(N1 + 1)]
        
        for row in range(1, N1 + 1):
            for col in range(1, N2 + 1):
                if text1[row - 1] == text2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])
        
        return dp[-1][-1]
        


assert Solution().longestCommonSubsequence( "abcde", "ace") == 3