from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for c in t:
            d[c] += 1
        l, r = 0, 0
        min_win = float('+inf')
        min_substr = ''
        N = len(s)
        while l <= r and r < N:
            if s[r] in d:
                d[s[r]] -= 1
            count = sum(list(d.values()))
            # print(f'count={count}, {r}, {l} -> {r-l+1}')
            if count <= 0:
                while l <= r and count <= 0:
                    if r -l + 1 <= min_win:
                        min_substr = s[l:r+1]
                    # print(f'min_substr={min_substr}')
                    min_win = min(min_win, r - l + 1)
                    if s[l] in d:
                        d[s[l]] += 1
                        count = sum(list(d.values()))
                    l += 1
            r += 1
        return '' if min_win == '+inf' else min_substr


s = Solution()
ans = s.minWindow("ADOBECODEBANC", "ABC")
print(ans)

ans = s.minWindow("bba", "ab")
print(ans)

ans = s.minWindow("acbbaca", "aba")
print(ans)