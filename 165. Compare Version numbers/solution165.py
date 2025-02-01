class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 = version1.split(".")
        version2 = version2.split(".")

        N = max(len(version1), len(version2))
        for i in range(0, N):
            v1 = v2 = 0
            if i >= len(version1):
                v1 = 0
            else:
                v1 = int(version1[i])
            if i >= len(version2):
                v2 = 0
            else:
                v2 = int(version2[i])
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1

        return 0
s = Solution()
v1 = "1.2."
v2 = "1.2.0"
print(s.compareVersion(v1, v2))
