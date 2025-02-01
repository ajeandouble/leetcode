from typing import List

class Solution:
    def largestRectangleArea(self, height: List[int]) -> int:
        N = len(height)
        maxArea = 0
        stack = []
        for i, h in enumerate(height):
            start = i
            while stack and stack[-1][1] > h:
                popped_idx, popped_h = stack.pop()
                print(maxArea, (i - popped_idx)  * popped_h)
                maxArea = max(maxArea, h, (i - popped_idx)  * popped_h)
                start = popped_idx

            stack.append((start, h))
            print(f'i={i}, stack={stack}')
        st_len = len(stack) + 1
        print(f'stack={stack}')
        for st_idx, st_height in stack:
            print(i, st_idx, st_height)
            maxArea = max(maxArea, (N - st_idx) * st_height)
        return maxArea


s = Solution()

# height = [2,1,2]
# ans = s.largestRectangleArea(height)
# print(height, '->', ans) # 3
# assert ans == 3

# height = [1,2,1]
# ans = s.largestRectangleArea(height)
# print(height, '->', ans) # 3
# assert ans == 3

# height = [2,1,5,6,2,3]
# ans = s.largestRectangleArea(height)
# print(height, '->', ans) # 10
# assert ans == 10

height = [10,20,5,4,3,2,1,2,3]
ans = s.largestRectangleArea(height)
print(height, '->', ans) #20
assert ans == 20