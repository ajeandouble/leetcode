class Solution:
    def longestPalindrome(self, s: str) -> str:
        pass
        return ""


s = "bbbb"
ans = Solution().longestPalindrome(s)
print(f"{s} => {ans}")
assert ans == "bbbb"

s = "cbbd"
ans = Solution().longestPalindrome(s)
print(f"{s} => {ans}")
assert ans == "bb"

s = "abc"
ans = Solution().longestPalindrome(s)
print(f"{s} => {ans}")

assert ans == "a" or ans == "b" or ans == "c"

s = "abcba"
ans = Solution().longestPalindrome(s)
assert ans == "abcba"
