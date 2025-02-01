from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        matrix_len = len(isConnected)
        visited = set()
        provinces = 0

        def bfs(city):
            stack = [city]
            while len(stack):
                # print(f'stack={stack}')
                city_a = stack.pop()
                visited.add(city_a)
                for city_b in range(matrix_len):
                    if city_b == city_a:
                        continue
                    elif isConnected[city_a][city_b] == 1 and city_b not in visited:
                        stack.append(city_b)
                        has_one_connection = True

        for city in range(matrix_len):
            if city in visited:
                continue
            else:
                provinces += 1
                bfs(city)

        return provinces






# -------
s = Solution()
isConnected = [[1,1,0],[1,1,0],[0,0,1]]
print(s.findCircleNum(isConnected))