from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) == 0:
            return 0
        if len(nums) % 2 == 0:
            return (nums[len(nums) // 2 - 1] + nums[len(nums) // 2]) / 2
        return nums[len(nums) // 2]

import math
sol = Solution()

ans = sol.findMedianSortedArrays([1,3], [2])
assert ans == 2

ans = sol.findMedianSortedArrays([1,2], [3,4])
assert ans == 2.5

ans = sol.findMedianSortedArrays([1,3,3,3,4], [-1,0,1,2,3,5,6,8,10])
assert ans == 3.00
