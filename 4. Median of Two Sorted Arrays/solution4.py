class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        N1, N2 = len(nums1), len(nums2)
        median_idxs = lambda arr, N : [arr[N//2-1], arr[N//2]] if N % 2 == 0 else [arr[N//2]]

        # print(median_idxs(nums1, N1))
        # print(median_idxs(nums2, N2))

        combined_len = N1 + N2
        combined_nums = []
        i1, i2 = 0, 0

        while i1 + i2 < combined_len:
            while i1 < N1 and ((i2 < N2 and nums1[i1] <= nums2[i2]) or i2 >= N2):
                combined_nums += [nums1[i1]]
                i1 += 1
            while i2 < N2 and ((i1 < N1 and nums2[i2] <= nums1[i1]) or i1 >= N1):
                combined_nums += [nums2[i2]]
                i2 += 1
            # import time
            # print(i1, i2, combined_nums)
            # time.sleep(0.3)

        if combined_len % 2 == 0:
            return float((combined_nums[combined_len//2-1] + combined_nums[combined_len//2]) / 2)
        else:
            return float(combined_nums[combined_len//2])

        print(N1+N2, combined_nums)
        return float(sum(median_idxs(combined_nums, combined_len)))





s = Solution()

# ans = s.findMedianSortedArrays([1,3], [2])
# print(ans)

# ans = s.findMedianSortedArrays([1,2], [3,4])
# print(ans)

# ans = s.findMedianSortedArrays([1,3,3,3,4], [-1,0,1,2,3,5,6,8,10])
# print(ans)