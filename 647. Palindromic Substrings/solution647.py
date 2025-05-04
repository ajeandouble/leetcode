class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        # memo = {(i, i): 1 for i in range(N)}
        memo = {}
        ans = 0

        def dfs(i, j):
            print(i, j)
            if i < 0 or j > N:
                return 0
            if (i, j) in memo:
                print(i, j, "not in memo")
                return memo[(i, j)]
            if i == j:
                print(i, j, "empty string")
                return 0
            if j - i == 1:
                memo[(i, j)] = 1
                print(i, j, "single character", memo)
            max_palin = max(dfs(i - 1, j + 1), dfs(i - 1, j), dfs(i, j + 1))
            print(i, j, max_palin)
            memo[(i, j)] = max_palin
            return memo[(i, j)]

        dfs(N // 2, N // 2 + 1)
        print(memo, "what")
        return ans


Solution().countSubstrings("aaa")
# Solution().countSubstrings("abc")
