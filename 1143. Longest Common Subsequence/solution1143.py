import numpy
import random

rnd = random.Random()

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
        ans = -1
        for i in range(1, len(text1)+1):
            for j in range(1, len(text2)+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                    ans = max(dp[i][j], ans)
                else:
                    dp[i][j] = rnd.choice([dp[i][j-1], dp[i-1][j]])
        # print(numpy.matrix(dp))
        return ans
        ans = ''
        i = len(text1)
        j = len(text2)
        while i and j:
            if text1[i-1] == text2[j-1]:
                ans += text1[i-1] # or text2[j-1]
                i -= 1
                j -= 1
            else:
                if max(dp[i][j-1], dp[i-1][j]) == dp[i][j-1]:
                    j-= 1
                else:
                    i -= 1
        print(ans)
        return len(ans)



s = Solution()
# ans = s.longestCommonSubsequence("abcde", "ace")
ans = s.longestCommonSubsequence( "abcbdab", "bdcaba")
print(f'ans={ans}')
