class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palin(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
                return True

        ans = 0
        for l in range(len(s)):
            for r in range(l, len(s)):
                print(l, r, s[l : r + 1])
                if is_palin(l, r):
                    ans = max(ans, r - l + 1)
        return ans


sol = Solution()
s = "babad"
ans = sol.longestPalindrome(s)
print(f"{s} => {ans}")
