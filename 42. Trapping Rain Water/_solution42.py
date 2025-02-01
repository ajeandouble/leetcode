class Solution:
    def trap(self, heights) -> int:
        N = len(heights)
        max_l = 0
        maxes_l = []
        for l in range(0, N):
            maxes_l.append(max_l)
            max_l = max(max_l, heights[l])

        max_r = 0
        maxes_r = [0] * N
        for r in range(N-1, -1, -1):
            maxes_r[r] = max_r
            max_r = max(max_r, heights[r])

        print(maxes_l)
        print(maxes_r)
        mins = []
        for i in range(0, N):
            mins.append(max(0, min(maxes_l[i], maxes_r[i]) - heights[i]))

        print(mins)
        return sum(mins)


s = Solution()


ans = s.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(ans)