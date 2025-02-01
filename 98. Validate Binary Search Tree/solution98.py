from typing import List, Dict, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"{TreeNode.__name__}({self.val, self.left, self.right})"

    def __str__(self):
        return self.__repr__()

node_d = TreeNode(99)
node_e = TreeNode(101)
node_b = TreeNode(1)
node_c = TreeNode(100, node_d, node_e)
root = TreeNode(5, node_b, node_c)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: TreeNode, left: int, right: int):
            if not node:
                return True
            print(node.val, left, right)
            if node.val > left and node.val < right:
                return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
            else:
                return False
        return dfs(root, float("-inf"), float("inf"))


ans = Solution().isValidBST(root)
print(ans)