# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __repr__(self):
        return 'TreeNode({})'.format(self.val)

def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left  = kids.pop()
            if kids: node.right = kids.pop()
    return root

from typing import Optional

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        st = [(root.left, 1)]
        left_d = 0
        while st:
            node, d = st.pop()
            if not node:
                continue
            left_d = max(left_d, d)
            st.append((node.left, d+1))
            st.append((node.right, d+1))

        st = [(root.right, 1)]
        right_d = 0
        while st:
            node, d = st.pop()
            if not node:
                continue
            right_d = max(right_d, d)
            st.append((node.left, d+1))
            st.append((node.right, d+1))
        print(left_d, right_d)
        return left_d + right_d

s = Solution()
assert s.diameterOfBinaryTree(deserialize('[1,2]')) == 1
assert s.diameterOfBinaryTree(deserialize('[1,2,3,4,5]')) == 3
assert s.diameterOfBinaryTree(deserialize('[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,'\
                                   'null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]')) == 8