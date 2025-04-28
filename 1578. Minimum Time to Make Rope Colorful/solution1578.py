from typing import List

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        N = len(colors)
        i = 1
        while i < N:
            if colors[i - 1] == colors[i]:
                curr_time = neededTime[i - 1]
                max_time = neededTime[i - 1]
                j = i
                while j < N and colors[j] == colors[i - 1]:
                    max_time = max(max_time, neededTime[j])
                    curr_time += neededTime[j]
                    j += 1
                ans += curr_time - max_time
                i = j
            else:
                i += 1
        return ans
                    
assert Solution().minCost("abc", [1,2,3]) == 0
assert Solution().minCost("abz", [1,2,42]) == 0
assert Solution().minCost("abaac", [1,2,3,4,5]) ==  3
assert Solution().minCost("aabaa", [1,2,3,4,1]) ==  2
assert Solution().minCost("bbbaaa", [4,9,3,8,8,9]) ==  23
                    