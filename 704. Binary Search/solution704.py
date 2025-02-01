from typing import List
import time



class Solution:
    def search(self, nums: List[int], t: int) -> int:
        N = len(nums)
        if N == 1:
            return 0 if nums[0] == t else -1
        l, r = 0, N-1
        while l <= r:
            mid = l + int((r - l) / 2)
            if nums[mid] == t:
                return mid
            if nums[mid] < t:
                l = mid +1
            else:
                r = mid -1
        return -1

s = Solution()

# print(s.search([-1,0,3,5,9,12], 9))
# print(s.search([-1,0,3,5,9,12], 2))
print(s.search([2,2,5], 5))