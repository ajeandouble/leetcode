# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        st = [(root, 0)]
        ans = [[]]
        while len(st):
            n, d = st.pop()
            if len(ans) < d:
                ans.append([])
            ans[d].append(n.val)
            if n.left:
                st.append((n.left, d + 1 ))
            if n.right:
                st.append((n.right, d + 1 ))
        return [sum(x) / len(x) for x in ans]

s = TreeNode()
s.append()
