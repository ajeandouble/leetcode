import numpy as np

class Solution:
    def maximalRectangle(self, m) -> int:
        R, C = len(m), len(m[0])
        for c in range(0, C):
            for r in range(0, R):
                if int(r)>=1 and int(m[r][c]) == 1 and int(m[r-1][c]) >= 1:
                    m[r][c] = int(m[r-1][c]) + 1
                elif int(m[r][c]) == 1:
                    m[r][c] = 1
                elif int(m[r][c]) == 0:
                    m[r][c] = 0
        stack = []
        ans = 0
        for r in m:
            print('')
            print('r=', r)
            for i, h in enumerate(r):
                start = i
                print(stack)
                print(i, h)
                while stack and stack[-1][1] > h:
                    print('b4 pop stack', stack,f'ans={ans}')

                    pop_idx, pop_h = stack.pop()
                    ans = max(ans, (i - pop_idx) * pop_h)
                    start = pop_idx
                    print('popped stack', stack, f'i={i} pop_idx={pop_idx} pop_h={pop_h}', f'ans={ans}', f'potential ans={(i - pop_idx) * pop_h}')
                stack.append((start, h))

            print('\t', stack, f'ans={ans}')
            # remaining monotonic stack, all elements can go from left to the end so
            st_len = len(r)
            for st_idx, st_h in stack:
                ans = max(ans, st_h * (st_len - st_idx))
            print(f'ans={ans}')
            stack = []
        print(np.matrix(m))
        return ans

s = Solution()


m = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
# print(f'm={m}')
ans = s.maximalRectangle(m)
assert ans == 6

m = [["0"]]
# print(f'm={m}')
ans = s.maximalRectangle(m)
assert ans == 0

m = [["1"]]
# print(f'm={m}')
ans = s.maximalRectangle(m)
assert ans == 1

m = [["1"],["1"]]
# print(f'm={m}')
ans = s.maximalRectangle(m)
assert ans == 2

m = [["1","1","1","1"],["1","1","1","1"],["1","1","1","1"],["1","1","1","1"],["1","1","1","1"],["1","0","1","1"]]
# print(f'm={m}')
ans = s.maximalRectangle(m)
assert ans == 20


m = [["1","1","1","1"],["0","1","0","1"],["1","1","1","1"],["1","1","1","1"],["1","1","1","1"],["1","0","1","1"]]
print(np.matrix(m))
# print(f'm={m}')
ans = s.maximalRectangle(m)
assert ans == 12


m = [["0","0","1","0"],["0","0","1","0"],["0","0","1","0"],["0","0","1","1"],["0","1","1","1"],["0","1","1","1"],["1","1","1","1"]]
print(np.matrix(m))
print(f'm={m}')
ans = s.maximalRectangle(m)
assert ans == 9

