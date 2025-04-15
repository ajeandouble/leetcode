from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        ans = []
        part = []

        def is_palindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l, r = l + 1, r - 1
            return True

        def dfs(i):
            if i >= N:
                ans.append(part.copy())
                return
            for j in range(i, N):
                if is_palindrome(i, j):
                    part.append(s[i : j + 1])
                    dfs(i + 1)
                    part.pop()

        dfs(0)
        return ans


S = Solution()

s = "aab"
ans = S.partition(s)
print(ans)
