from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prereq: list[list[int]]) -> bool:
        scheduleMap = defaultdict(list)
        for curr, pre in prereq:
            scheduleMap[curr].append(pre)
        visited = set()
        curr_visited = set()  # loop detection

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
            curr_visited.remove(node)
            return True

        for curr, _ in scheduleMap.items():
            if not dfs(curr):
                return False

        return True


assert Solution().canFinish(2, [[1, 0]]) == True
assert Solution().canFinish(2, [[1,0],[0,1]]) == False
assert Solution().canFinish(5, [[0,1], [0,2], [1,3], [1,4], [3,4]]) == True
