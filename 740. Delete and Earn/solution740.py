from typing import List

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        N = len(nums)
        freq = {}
        for n in nums:
            if n in freq[n]:
                freq[n] += 1
            else:
                freq[n] = 1
