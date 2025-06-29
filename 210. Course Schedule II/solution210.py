class Solution:
    def findOrder(self, numCourses: int, prereq: list[list[int]]) -> list[int]:
        from collections import defaultdict
        scheduleMap = {i: [] for i in range(numCourses)}
        for curr, pre in prereq:
            scheduleMap[curr].append(pre)
        visited = set()
        curr_visited = set()  # loop detection
        curr_path = []
        ans = []
        def dfs(node):
            if node in curr_visited:
                return False
            if node in visited:
                return True
            if node not in scheduleMap:
                return True
            visited.add(node)
            curr_visited.add(node)
            for req in scheduleMap[node]:
                if not dfs(req):
                    return False
            curr_path.append(node)
            curr_visited.remove(node)
            return True

        for curr, _ in scheduleMap.items():
            curr_path = []
            if not dfs(curr):
                return []
            else:
                ans.extend(curr_path)

        return ans

assert Solution().findOrder(2, [[1,0]]) == [0,1]
assert sorted(Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]])) == sorted([0,1,2,3])
assert Solution().findOrder(1, []) == [0]