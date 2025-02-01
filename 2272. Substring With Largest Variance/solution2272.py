#+----+---+---+---+---+----+---+---+---+---+---+
#| b  | a | a | b | b | b  | a | a | a | a | a |
#+----+---+---+---+---+----+---+---+---+---+---+
#| -1 | 0 | 1 | 1 | 0 | -1 | 0 | 1 | 2 | 3 | 4 |
#+----+---+---+---+---+----+---+---+---+---+---+

class Solution:
    def largestVariance(self, s: str) -> int:
        def kadanes(a, b, s):
            max_ending_here = 0
            max_so_far = 0
            has_b = False
            subarray_starts_with_b = False
            for ch in s:
                if ch == a:
                    max_ending_here += 1
                elif b == ch:
                    has_b = True
                    if not subarray_starts_with_b and max_ending_here <= 0:
                        max_ending_here = -1
                        subarray_starts_with_b = True
                    elif subarray_starts_with_b and max_ending_here >= 0:
                        subarray_starts_with_b = False
                    else:
                        max_ending_here -= 1

                max_ending_here = max(max_ending_here, -1)
                if has_b:
                    max_so_far = max(max_so_far, max_ending_here)
            return max_so_far if has_b else 0

        chars = list(set(s))
        ans = 0
        for c1 in chars:
            for c2 in chars:
                if c1 == c2:
                    continue
                ans = max(ans, kadanes(c1, c2, s))
        return ans


s = Solution()
ans = s.largestVariance('bbabaaa')
print(f'ans={ans}') # except 3
ans = s.largestVariance('abbabaaba')
print(f'ans={ans}') # except 3
ans = s.largestVariance('')
print(f'ans={ans}') # except 3
# ans = s.largestVariance('lripaa')
# print(f'ans={ans}') # except 2


# def kadanes(arr):
#     max_ending_here = 0
#     max_so_far = 0
#     for i, n in enumerate(arr):
#         max_ending_here = max_ending_here + n
#         max_so_far = max(max_so_far, max_ending_here)
#         max_ending_here = max(max_ending_here, 0)
#     return max_so_far

# ans = kadanes([-1,-1,-1,-1,0,1,1,1,1,-1,1])
# print(ans)