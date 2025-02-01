class TrieNode:
    def __init__(self):
        self.children = {}

    def __str__(self):
        return f"{TrieNode.__name__}({self.children})"

    def __repr__(self):
        return str(self)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for i, c in enumerate(word):
            if c not in node.children.keys():
                node.children[c] = TrieNode()
            node = node.children[c]
        node.children[""] = None

    def search(self, word: str) -> bool:
        node = self.root
        # # print(self.root)
        for i, c in enumerate(word):
            if c not in node.children.keys():
                return False
            node = node.children[c]
        if "" not in node.children:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for i, c in enumerate(prefix):
            if c not in node.children.keys():
                return False
            node = node.children[c]
        return True

    def __str__(self):
        return f"{Trie.__name__}({self.root})"


# Your Trie object will be instantiated and called as such:
obj = Trie()
print(obj)
search = obj.search("ab")
print(search)
search = obj.startsWith("ab")
print(search)
obj.insert("ab")
print(obj)
search = obj.search("ab")
print(search)
# param_3 = obj.startsWith("a")
# print(param_3)
# ans = obj.search("ab")
# print(ans)
