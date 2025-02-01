# from typing import List, Dict, Optional

# class Solution:
#     def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
#         s = set()
#         ans = [[]]
#         for n in nums:
#             N = len(ans)
#             for i in range(0, N):
#                 result = ans[i] + [n]
#                 if True or tuple(sorted(result)) not in s:
#                     ans.append(ans[i] + result)
#                     s.add(tuple(sorted(result)))
#         print(ans)
#         return ans

# s = Solution()

# nums = [1,2,2]
# ans = s.subsetsWithDup(nums)
# assert sorted(ans) == sorted([[],[1],[1,2],[1,2,2],[2],[2,2]])


import sys
# def test(default_arr=[], d=0):
#     print(id(default_arr), id(d), sys.getrefcount(default_arr), sys.getrefcount(d))
#     if d > 10:
#         return
#     test(d=d+1)

# test()

# print(sys.getrefcount(42))
mul = 1
d = {}
for i in range(-10, 11, 1):
    d[i] = mul
    mul *= 10
print(d)