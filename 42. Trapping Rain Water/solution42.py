class Solution:
    def trap(self, heights) -> int:
        l, r = 0, 0
        ans = 0
        while l < len(heights) and heights[l] == 0:
            l += 1
        if l == len(heights):
            return 0
        while l < len(heights) and r < len(heights):
            r = l + 1
            l_max = heights[l]
            minus = []
            print(l, r, l_max, minus)
            r_max = float('-inf')
            while r < len(heights) and heights[r] < l_max:
                minus.append(heights[r])
                r += 1
            if r == len(heights): break
            ans += (r - l - 1) * heights[l] - sum(minus)
            print(l_max, l, r)
            l = r

        return ans

s = Solution()
input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
# input = [4, 2, 0, 3, 2, 5]
# input = [2, 0, 2]
input = [4, 2, 3]
input = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
ans = s.trap(input)
print(ans)
