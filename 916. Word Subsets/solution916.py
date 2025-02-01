from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        frequencies = {}
        for l in words1:
            if l not in frequencies:
                frequencies[l] = 1
            else:
                frequencies[l] += 1
        print(frequencies)
        pass

s = Solution()
# s.wordSubsets()