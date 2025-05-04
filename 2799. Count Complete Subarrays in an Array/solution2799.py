from typing import List
from collections import defaultdict

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        N = len(nums)
        NUM_OF_ELS = len(set(nums))
        els = defaultdict(int)
        ans = 0
        l = r = 0
        while r < N:
            saved_r = None
            while r < N and len(els) <= NUM_OF_ELS:
                els[nums[r]] += 1
                if len(els) == NUM_OF_ELS:
                    print(nums[l:r+1], l, r, ans + 1)
                    saved_r = r if not saved_r else saved_r
                    ans += 1
                print(r)
                r += 1
            print(f"l={l}, r={r}, saved_r={saved_r}")
            print(els)
            while l < r and len(els) == NUM_OF_ELS:
                print("WTF")
                els[nums[l]] -= 1
                l += 1
                els[nums[l]] -= 1
                if els[nums[l]] != 0:
                    els[nums[l]] += 1
                    print("l < r", nums[l:r+1], l, r, ans)
                    ans += 1
                else:
                    del els[nums[l]]
                l += 1
            l = r = saved_r if saved_r else r
            r += 1
            
        return ans

# ans = Solution().countCompleteSubarrays([5,5,5,5])
# print(ans)

ans = Solution().countCompleteSubarrays([1,3,1,2,2])
print(ans)