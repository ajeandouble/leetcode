from typing import List, Dict, Set
from collections import defaultdict


# If a ball changes color we have to know if that colour already exists
# To know if that color already exists we will need to now if another ball has that color assigned
# So we need to keep track of balls by colors and also of the previous ball color


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors: Dict[Set[int]] = defaultdict(set)
        balls: Dict[int] = {}
        print(colors, "\n", balls)
        ans = []
        curr_ans = 0
        for q in queries:
            b = q[0]
            c = q[1]
            prev_c = balls[b] if b in balls else None
            if prev_c:
                colors[prev_c].remove(b)
                # if only that ball had that color we decrement the number of different colors
                if not colors[prev_c]:
                    curr_ans -= 1
            # if only that ball will have that colour we added a new different colour
            if not colors[c]:
                curr_ans += 1
            colors[c].add(b)
            balls[b] = c
            ans.append(curr_ans)
        return ans


sol = Solution()
limit = 4
queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
ans = sol.queryResults(limit, queries)
print(f"lim == {limit}, queries == {queries} -> {ans}")
