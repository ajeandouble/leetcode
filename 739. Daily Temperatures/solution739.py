from typing import List

class Solution:
    def dailyTemperatures(self, tps: List[int]) -> List[int]:
        N = len(tps)
        tps.append(-1)
        ans = [0] * N
        stack = []
        for i in range(0, N):
            t = tps[i]
            print(f'{i} < {N}\tt = {tps[i]}')
            start = i
            while stack and stack[-1][1] < t:
                print(f'stack[-1][1] = {stack[-1][1]} < t = {t}\t', end='')
                # print(stack, stack[-1][1], t)
                print(stack)
                pop_idx, pop_t = stack.pop()
                print(f'{(pop_idx, pop_t)} was popped from {stack}')
                # print('\t', stack)
                ans[pop_idx] = i - pop_idx
                print(f'ans={ans}')
                start = pop_idx
                print(f'new start = {start}')
            stack.append((start, t))
            print(stack)
        return ans

s = Solution()
tps = [73,74,75,71,69,72,76,73]
print(f'tps={tps}')
ans = s.dailyTemperatures(tps)
print(f'ans={ans}')