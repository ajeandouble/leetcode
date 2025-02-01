
class Solution:
    def findMin(self, nums) -> int:
        N = len(nums)
        if N == 1:
            return nums[0]
        l, r = 0, N - 1
        max_so_far = -1
        if nums[-1] > nums[0]:
            return nums[0]
        # size = N
        while l <= r:
            mid = l + int((r-l)/2)
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            if nums[mid] < nums[r]:
                r = mid -1
            else:
                l = mid + 1


        return -1


s = Solution()
print(s.findMin([4,5,6,7,0,1,2])) # 0
print(s.findMin([11,13,15,17])) # 11
print(s.findMin([2,3,4,5,1])) # 1
print(s.findMin([2, 3, 4, 5, 1]))  # 1

print(s.findMin([5,1,2,3,4]))  # 1
