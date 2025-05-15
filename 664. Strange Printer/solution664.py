from functools import cache


class Solution:
    def strangePrinter(self, s: str) -> int:
        if not s:
            return 0

        old_s = s
        s = old_s[0]
        for i in range(1, len(old_s)):
            if old_s[i] != old_s[i - 1]:
                s += old_s[i]

        n = len(s)
        memo = {}

        @cache
        def dp(l, r):
            if l > r:
                return 0
            if l == r:
                return 1
            result = 1 + dp(l + 1, r)
            for mid in range(l + 1, r + 1):
                if s[l] == s[mid]:
                    result = min(result, dp(l + 1, mid - 1) + dp(mid, r))
            memo[(l, r)] = result
            return result

        return dp(0, n - 1)


assert Solution().strangePrinter("aaabbb") == 2
assert Solution().strangePrinter("aba") == 2
