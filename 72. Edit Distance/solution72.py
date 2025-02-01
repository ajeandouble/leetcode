import numpy

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = [[j if i == 0 else 0 for j in range(0, len(word2)+1)] for i in range(0, len(word1)+1)]
        for i, r in enumerate(dp):
            r[0] = i

        # print(numpy.matrix(dp))

        for i in range(1, len(word1)+1):
            for j in range(1, len(word2)+1):
                print(f'{i-1} {j-1}', word1[i-1], word2[j-1])
                # print(replace, delete, insert, min(replace, delete, insert))

                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    replace = dp[i-1][j-1]
                    delete = dp[i][j-1]
                    insert = dp[i-1][j]
                    dp[i][j] = 1 + min(replace, delete, insert)

        print(numpy.matrix(dp))
        return(dp[len(word1)][len(word2)])

s = Solution()
print(s.minDistance("ephrem", "benyam"))