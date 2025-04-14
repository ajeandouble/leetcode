from typing import List
from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        heap = []
        for n in nums:
            d[n] += 1
            heapq.heappush(heap, (-d[n], n))
            # print(heap)
        # print("---")
        ans = []
        for _ in range(k):
            popped = heapq.heappop(heap)
            curr = popped[1]
            ans.append(curr)
            while heap and heap[0][1] == curr:
                heapq.heappop(heap)
            # print(heap)
        return ans
        # return [heapq.heappop(heap)[1] for _ in range(k)]


nums = [1, 1, 1, 2, 2, 3]
k = 2
ans = Solution().topKFrequent(nums, k)
print(f"{nums}, {k} => {ans}")
assert ans == [1, 2]
