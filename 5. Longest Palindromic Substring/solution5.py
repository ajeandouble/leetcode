class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        max_len = 1
        ans = s[0]

        def helper_even(i):
            if i - 1 >= 0 and s[i - 1] == s[i]:
                l = i - 2
                r = i + 1
                while l >= 0 and r < len(s) and s[l] == s[r]:
                    l, r = l - 1, r + 1
                return s[l+1:r]
            return s[i]

        def helper_odd(i):
            l, r = i - 1, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l, r = l - 1, r + 1
            return s[l + 1:r]

        for i in range(N):
            even_s = helper_even(i)
            if len(even_s) > max_len:
                ans = even_s
                max_len = len(even_s)
            odd_s = helper_odd(i)
            if len(odd_s) > max_len:
                ans = odd_s
                max_len = len(odd_s)
        return ans

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

assert (ans == "a" or ans == "b" or ans == "c")

s = "abcba"
ans = Solution().longestPalindrome(s)
assert ans == "abcba"