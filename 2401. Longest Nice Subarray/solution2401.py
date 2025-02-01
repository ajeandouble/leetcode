from typing import List

BIT_FREQ_SIZE = 32


class BitFreq:
    def __init__(self, n=0):
        mask = 1
        self.frequencies = [0] * BIT_FREQ_SIZE
        if n == 0:
            return
        for i in range(BIT_FREQ_SIZE):
            self.frequencies[BIT_FREQ_SIZE - 1 - i] = 1 if n & mask else 0
            mask <<= 1

    def is_nice(self):
        for f in self.frequencies:
            if f > 1:
                return False
        return True

    def __add__(self, other):
        if not isinstance(other, BitFreq):
            return NotImplementedError

        new_bit_freq = BitFreq()
        for i in range(BIT_FREQ_SIZE):
            new_bit_freq.frequencies[i] = self.frequencies[i] + other.frequencies[i]

        return new_bit_freq

    def __sub__(self, other):
        if not isinstance(other, BitFreq):
            return NotImplementedError

        new_bit_freq = BitFreq()
        for i in range(BIT_FREQ_SIZE):
            new_bit_freq.frequencies[i] = self.frequencies[i] - other.frequencies[i]

        return new_bit_freq

    def __repr__(self):
        return f"BitFreq({self.frequencies})"


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 1
        bit_freq = BitFreq(0)
        l = 0
        print(BitFreq(nums[0]) + BitFreq(nums[1]) - BitFreq(nums[0]))
        for r in range(len(nums)):
            bit_freq += BitFreq(nums[r])
            print('r', bit_freq)
            while l <= r and not bit_freq.is_nice():
                bit_freq -= BitFreq(nums[l])
                l += 1
                print('l', bit_freq)
            if bit_freq.is_nice():
                ans = max(ans, r - l + 1)

        return ans

        # print(bit_freq)
        # print(nums[r], bit_freq.is_nice())


s = Solution()
nums = [1, 3, 8, 48, 10]
result = s.longestNiceSubarray(nums)
print(f"nums={nums} -> result = {result}")

nums = [1, 3, 8, 48, 10]
result = s.longestNiceSubarray(nums)
print(f"nums={nums} -> result = {result}")
assert result == 3

nums = [3, 1, 5, 11, 13]
result = s.longestNiceSubarray(nums)
print(f"nums={nums} -> result = {result}")
assert result == 1
