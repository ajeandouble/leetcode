from typing import List
from collections import defaultdict


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        nums = list(set(nums))
        N = len(nums)
        if N < 4:
            return 0
        visited = defaultdict(int)
        for i in range(N - 1):
            for j in range(i + 1, N):
                product = nums[i] * nums[j]
                visited[product] += 1
        return sum([(x * (x - 1)) // 2 for x in visited.values()]) * 8


sol = Solution()

input = [2, 3, 4, 6]
ans = sol.tupleSameProduct(input)
print(f"{input} -> ans == {ans}")

input = [1, 2, 4, 5, 10]
ans = sol.tupleSameProduct(input)
print(f"{input} -> ans == {ans}")

input = [2, 3, 4, 6, 8, 12]
ans = sol.tupleSameProduct(input)
print(f"{input} -> ans == {ans}")
