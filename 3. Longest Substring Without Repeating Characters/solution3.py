from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        chars = set()
        l = 0
        ans = 1
        for r in range(N):
            print(l, r, chars)
            if s[r] not in chars:
                chars.add(s[r])
                ans = max(ans, r - l + 1)
            else:
                last = 0
                while l <= r:
                    if s[l] == s[r]:
                        last = l
                    if s[l] in chars: chars.remove(s[l])
                    l += 1
                ans = max(ans, r - last)
                chars.add(s[r])

        return ans

sol = Solution()
s = "pwwkew"
result = sol.lengthOfLongestSubstring(s)
print(f"result = {result}")
