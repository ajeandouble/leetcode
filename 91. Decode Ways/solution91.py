class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        val = int(s[:2])
        if N == 1:
            return 1
        isBadVal = lambda x: x == 0 or x <= 9 or (x >= 30 and x % 10 == 0)
        if N == 0 or isBadVal(val):
            return 0
        q = 0
        r = 1
        for i in range(1, N):
            if i + 1 < N:
                val = int(s[i - 1:i + 1])
                if isBadVal(val):
                    return 0
                curr = (q + 1) + (r + 1)
        return (q, r)

s = "340"   # BBF, VF, BZ
ans = Solution().numDecodings(s)
print(f"{s} => {ans}")


# s = "11"
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")


# s = "20"
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")


# s = "11111"
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")


# s = "111111"
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")

# s = "1111111"
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")


# s = "11111111"
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")

# s = "111111111"
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")


s = "226"  # (2,2,6; 22,6; 2,26)
ans = Solution().numDecodings(s)
print(f"{s} => {ans}")

# s = "1111111111111"
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")

# s = "10"  # (10)
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")

# 0, 1
# s = "12"  # (1,2; 12)
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")


# s = "2269"  # (2,2,6,9; 2,26,9; 22,6,9)
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")

# s = "22262"
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")

# s = "222322223222232222323223"
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")

# s = "2301"  # ()
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")

# s = "30"  # ()
# ans = Solution().numDecodings(s)
# print(f"{s} => {ans}")
