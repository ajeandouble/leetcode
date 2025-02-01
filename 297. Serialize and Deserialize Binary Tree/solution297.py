class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return f"Node({self.val}, {self.left}, {self.right})"

    def __eq__(self, other):
        return (self.val, self.left, self.right) == (other.val, other.left, other.right)

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return []
        data = []

        def dfs(node, depth=0, offset=0):
            idx = (2 ** depth) - 1 + offset
            if idx >= len(data):
                while idx >= len(data):
                    data.append(None)
            # print(idx, len(data))
            data[idx] = node.val
            if node.left:
                dfs(node.left, depth + 1, offset * 2)
            if node.right:
                dfs(node.right, depth + 1, offset * 2 + 1)
        dfs(root, 0, 0)
        # print(data)
        return str(data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        import ast
        data = ast.literal_eval(data)
        root = TreeNode(data[0])

        def visit(node, depth=0, offset=0):
            idx = (2 ** depth) - 1 + offset
            if idx >= len(data):
                return None
            if not data[idx]:
                return None
            node = TreeNode(data[idx])
            node.left = visit(node.left, depth + 1, offset * 2)
            node.right = visit(node.right, depth + 1, offset * 2 + 1)
            return node

        return visit(root, 0, 0)


node_D = TreeNode(5)
node_C = TreeNode(4)
node_B = TreeNode(3, node_C, node_D)
node_A = TreeNode(2)
root = TreeNode(1, node_A, node_B)

print(root)
# Your Codec object will be instantiated and called as such:
ser = Codec().deserialize(Codec().serialize(root))
assert root == ser

# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
