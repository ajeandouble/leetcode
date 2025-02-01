from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([(root, 0)])
        max_left_val = {0: root.val}
        max_depth = 0
        while len(queue):
            curr, d = queue.popleft()
            if d not in max_left_val:
                max_left_val[d] = curr.val
                max_depth = d
            if curr.left:
                queue.append((curr.left, d + 1))
            if curr.right:
                queue.append((curr.right, d + 1))
        return max_left_val[max_depth]


left = TreeNode(1)
right = TreeNode(3)
root = TreeNode(2, left, right)

s = Solution()
ans = s.findBottomLeftValue(root)
print(ans)
