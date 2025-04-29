class TrieNode():
    def __init__(self):
        self.nodes = [None] * 26
    
    @staticmethod
    def __insert(node: "TrieNode", s):
        if not s:
            return
        idx = ord(s[0]) - ord('a')
        if node.nodes[idx] is None:
            node.nodes[idx] = TrieNode()
        TrieNode.__insert(node.nodes[idx], s[1:])
    
    def insert(self, s) -> None:
        TrieNode.__insert(self, s)
        # print(self.nodes)

    def __str__(self):
        return "".join([chr(ord('a') + i) for i in range(0, 26) if self.nodes[i]])

root = TrieNode()
root.insert("abcd")
root.insert("bbcd")
root.insert("bbc")
assert root
assert root.nodes[0]
assert root.nodes[1]
assert root.nodes[2] == None
assert root.nodes[0].nodes[1]
assert root.nodes[0].nodes[1].nodes[2].nodes[3]
assert root.nodes[0].nodes[1].nodes[2].nodes[4] == None
assert root.nodes[0].nodes[2] == None
assert root.nodes[1].nodes[1].nodes[5] == None
assert root.nodes[1].nodes[1].nodes[2]