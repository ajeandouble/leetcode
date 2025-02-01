class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # TODO: edge case with k = 0?
        ans, N = 0, len(s)
        freqs = [0] * 26

        l, r = 0, 0
        while r < N:
            c = ord(s[r]) - ord('A')
            freqs[c] += 1
            # max_freqs_idx = freqs.index(max(freqs))
            window_len = r - l + 1
            if window_len - max(freqs) > k:
                c = ord(s[l]) - ord('A')
                freqs[c] -= 1
                l += 1
            else:
                ans = max(ans, window_len)
            r += 1
        return ans


solution = Solution()

s = "ABAB"
k = 2
assert solution.characterReplacement(s, k) == 4


s = "AABABBA"
k = 1
assert solution.characterReplacement(s, k) == 4