isGoodSubstring = (
    lambda x: len(x) < 2 or int(x) % 10 != 0 or int(x) < 30 and int(x) != 0
)
isDecodable = (
    lambda x: int(x) != 0 and int(x) <= 26 and not (len(x) >= 2 and int(x) < 10)
)


class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)

        # Check if empty string and bad substring on first char
        if N == 0 or not isDecodable(s[0]):
            return 0
        if N == 1:
            return 1
        if not isGoodSubstring(s[:2]):
            return 0

        dp = [0] * N
        dp[0] = 1  # necessarily decodable
        dp[1] = 2 if isDecodable(s[:2]) and isDecodable(s[1]) else 1

        for i in range(2, N):
            if i < N and not isGoodSubstring(s[i - 1 : i + 1]):
                return 0
            # If (...s[i-1], s[i]) is a possible num decoding of substring s[:2]
            if isDecodable(s[i]):
                dp[i] += dp[i - 1]
            if isDecodable(s[i - 1 : i + 1]):
                dp[i] += dp[i - 2] if i - 2 >= 0 else 0
            # If (...s[i-2], s[i-1]-s[i]) is a possible num decoding of substrings[:2]
        return dp[-1]


ans = Solution().numDecodings("")  # (EMPTY)                       ->  0
assert ans == 0
ans = Solution().numDecodings("0")  # (INDECODABLE)                 ->  0
assert ans == 0
ans = Solution().numDecodings("00")  # (INDECODABLE)                 ->  0
assert ans == 0
ans = Solution().numDecodings("01")  # (INDECODABLE)                 ->  0
assert ans == 0
ans = Solution().numDecodings("10")  # J                             ->  1
assert ans == 1
ans = Solution().numDecodings("11")  # AA, K                         ->  2
assert ans == 2
ans = Solution().numDecodings("40")  # (BAD SUBSTRING)               ->  0
assert ans == 0
ans = Solution().numDecodings("340")  # (BAD SUBSTRING)               ->  3
assert ans == 0
ans = Solution().numDecodings("2222")  # BBBB, BBV, BVB, VBB, VV       ->  5
assert ans == 5
ans = Solution().numDecodings("2262")  # BBFB, VFB, BZB                ->  3
assert ans == 3
ans = Solution().numDecodings("11101")  # AAJA, KJA                    ->  2
assert ans == 2

assert isGoodSubstring("0") == True
assert isGoodSubstring("00") == False
assert isGoodSubstring("01") == True
assert isGoodSubstring("10") == True
assert isGoodSubstring("20") == True
assert isGoodSubstring("21") == True
assert isGoodSubstring("29") == True
assert isGoodSubstring("30") == False
assert isGoodSubstring("40") == False
assert isGoodSubstring("90") == False
assert isGoodSubstring("98") == True
assert isGoodSubstring("99") == True

assert isDecodable("0") == False
assert isDecodable("9") == True
assert isDecodable("10") == True
assert isDecodable("11") == True
assert isDecodable("26") == True
assert isDecodable("27") == False
