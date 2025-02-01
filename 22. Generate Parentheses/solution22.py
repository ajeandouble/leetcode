class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        saved_n = n
        def bt(s, n, total):
            print(s, '\t', n, total)
            if not n and not total:
                ans.append(s)
            if n > 0:
                bt(s+'(', n-1, total+1)
            if total > 0:
                bt(s+')', n, total-1)
        bt('', n, 0)
        print(ans)
        return ans


s = Solution()
print(s.generateParenthesis(2))