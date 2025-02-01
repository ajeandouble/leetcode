from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        N, ans = len(height), 0
        l, r = 0, N - 1
        i1 = -1
        i2 = -1
        ans = 0
        st = [height[0]]
        while l < r:
            hl = height[l]
            hr = height[r]
            area = (r - l) * min(hl, hr)
            ans = max(ans, area)
            if hl < hr: l += 1
            else: r -= 1
        return ans





s = Solution()

# height = [1,8,6,2,5,4,8,3,7]
# ret = s.maxArea(height)
# print(f'{height} -> \t{ret}')

# height = [1,1]
# ret = s.maxArea(height)
# print(f'{height} -> \t{ret}')

height = [2,3,4,5,18,17,6]
ret = s.maxArea(height)
print(f'{height} -> \t{ret}')