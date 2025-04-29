from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        print(nums)
        ans = 0
        max_product = curr_max = curr_min = nums[0]
        for n in nums[1:]:
            saved_max, saved_min = curr_max, curr_min
            
            curr_max = max(saved_max * n, saved_min * n, n)
            curr_min = min(saved_max * n, saved_min * n, n)
            print(saved_max, saved_min, curr_max, curr_min)
            ans = max(ans, curr_max)
        return ans
    
assert Solution().maxProduct([2,3,-2,4]) == 6