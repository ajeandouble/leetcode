from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        diff = [0] * N
        for q in queries:
            l, r = q
            diff[l] += 1
            if r + 1 < N:
                diff[r + 1] -= 1
        curr_diff = 0
        for i, d in enumerate(diff):
            curr_diff += d
            nums[i] -= curr_diff
            if nums[i] > 0:
                return False
        return True


isZeroArray = Solution().isZeroArray
assert isZeroArray([1, 0, 1], [[0, 2]]) == True
assert isZeroArray([4, 3, 2, 1], [[1, 3], [0, 2]]) == False

# # Naive bruteforce approach
# class Solution:
#     def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
#         for q in queries:
#             for i in range(q[0], q[1] + 1):
#                 nums[i] -= 1
#         return all(map(lambda x: x <= 0, nums))
