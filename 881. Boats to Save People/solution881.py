from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        N = len(people)
        people.sort(reverse=True)
        if len(people) == 1:
            return 1
        lo = 0
        ans = 0
        visited_idxs = set()
        while lo < N:
            if people[lo] > limit:
                ans += 1
            else:
                break
            lo += 1

        while lo < N:
            if lo in visited_idxs:
                lo += 1
                continue
            hi = lo + 1
            found = False
            while hi < N and not found:
                if (
                    lo not in visited_idxs
                    and hi not in visited_idxs
                    and people[lo] + people[hi] <= limit
                ):
                    found = True
                    visited_idxs.add(lo)
                    visited_idxs.add(hi)
                hi += 1
            found = False
            while lo < hi and hi < N and not found:
                if (
                    lo not in visited_idxs
                    and hi not in visited_idxs
                    and people[lo] + people[hi] <= limit
                ):
                    found = True
                    visited_idxs.add(lo)
                    visited_idxs.add(hi)
                lo += 1
            lo += 1
        return len(visited_idxs)

s = Solution()
people = [3, 5, 3, 4]
people = [3, 5, 3, 4]
people = [1, 5, 3, 5]
limit = 3
ans = s.numRescueBoats(people, limit)
print(ans)
