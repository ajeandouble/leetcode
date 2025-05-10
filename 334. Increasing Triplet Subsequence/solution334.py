from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        N = len(nums)
        first = second = float("+inf")
        i = 0
        while i < N:
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True
            i += 1
        return False


assert Solution().increasingTriplet([1, 2, 3, 4, 5]) == True
assert Solution().increasingTriplet([5, 4, 3, 2, 1]) == False
assert Solution().increasingTriplet([2, 1, 5, 0, 4, 6]) == True
