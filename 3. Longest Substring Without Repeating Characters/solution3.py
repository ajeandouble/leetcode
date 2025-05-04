from typing import List
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        N = len(s)
        ans = 0
        characters = set()
        l, r = 0, 0
        while r < N:
            if s[r] in characters:
                while l < r:
                    characters.remove(s[l])
                    l += 1
                    if s[l - 1] == s[r]:
                        break
            ans = max(ans, r - l + 1)
            characters.add(s[r])
            r += 1
        return ans

sol = Solution()
s = "pwwkew"
ans = sol.lengthOfLongestSubstring(s)
assert ans == 3
