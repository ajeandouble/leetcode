from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        print("\t\t\t", ans)
        for n in nums:
            for i in range(0, len(ans)):
                ans.append(ans[i] + [n])
                print(f"n={n} i={i}\t\t\t", ans)
        print()
        return ans

s = Solution()
nums = [1,2,3]
ans = s.subsets(nums)
print(ans)
