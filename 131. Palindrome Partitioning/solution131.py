from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        ans = []
        part = []

        def is_palindrome(s):
            l = len(s)
            if l % 2 == 0:
                return s[: l // 2] == s[: l // 2 - 1 : -1]
            else:
                return s[: l // 2] == s[: l // 2 : -1]

        def dfs(i):
            nonlocal part
            if i >= len(s):
                ans.append(part.copy())
            for j in range(i, N):
                if is_palindrome(s[i : j + 1]):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return ans

S = Solution()

s = "aab"
ans = S.partition(s)
print(ans)

