from typing import Optional, List, Dict
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

node_15 = TreeNode(15)
node_7 = TreeNode(7)
node_20 = TreeNode(20, node_15, node_7)
node_9 = TreeNode(9)
root = TreeNode(3, node_9, node_20)

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        dct: Dict = {}
        st: List[List[TreeNode]] = [[root.val]]
        ans = [[root.val]]
        depth = 0
        while st:
            node = st.pop()
            if node[1].left or node[1].right and node[0] + 1 >= len(ans):
                ans.append([])
            if node[1].left:
                ans[node[0] + 1].append(node[1].left.val)
                st.append((node[0] + 1, node[1].left))
            if node[1].right:
                ans[node[0] + 1].append(node[1].right.val)
                st.append((node[0] + 1, node[1].right))
        return ans

print(Solution().levelOrder(root))