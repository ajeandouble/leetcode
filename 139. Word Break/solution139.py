# # class Solution:
# #     def wordBreak(self, s: str, words: List[str]) -> bool:
# #         N = len(s)
# #         i = 0
# #         ans = False
# #         def dfs(i):
# #             if i > N:
# #                 return False
# #             if i == N:
# #                 return True
# #             for w in words:
# #                 n = len(w)
# #                 if i + n <= N and s[i:].startswith(w):
# #                     if dfs(i + n):
# #                         return True
# #                     else:
# #                         continue
# #             return False

# #         return dfs(0)
    
# # # TLE!    

# from typing import List
# class TrieNode():
#     def __init__(self):
#         self._isstring = False
#         self.nodes = [None] * 26
    
#     @property
#     def isstring(self):
#         return self._isstring

#     @staticmethod
#     def __insert(node: "TrieNode", s):
#         if not s:
#             node._isstring = True
#             return
#         idx = ord(s[0]) - ord('a')
#         if node.nodes[idx] is None:
#             node.nodes[idx] = TrieNode()
#         TrieNode.__insert(node.nodes[idx], s[1:])
    
#     def insert(self, s: str) -> None:
#         TrieNode.__insert(self, s)

#     def dfs(self, root: "TrieNode", s: str, start_idx: int, i: int, ans=[]) -> None:
#         print(i)
#         if i >= len(s):
#             return
#         idx = ord(s[i]) - ord('a')
#         if self.isstring:
#             ans.append(s[start_idx:i])
            
#         if self.nodes[idx] is None:
#             root.dfs(root, s, i + 1, i + 1, ans)
#             return ans
#         return self.nodes[idx].dfs(root, s, start_idx, i + 1, ans)
            
        
#     def __str__(self):
#         return "".join([chr(ord('a') + i) for i in range(0, 26) if self.nodes[i]])

# class Solution:
#     def wordBreak(self, s: str, words: List[str]) -> bool:
#         N = len(s)
#         root = TrieNode()
#         for w in words:
#             root.insert(w)
#         i = 0
#         # while i < N:
#         some_word = root.dfs(root, s, 0, 0)
#         print(some_word)
#             # i = some_word
#         # print("TRUE")
#         # return True
#         # ans = root.dfs(s, 0)
#         # print(ans)
#         # return ans
        
        
# # Solution().wordBreak("leetcode", ["leet", "let", "code"])
# Solution().wordBreak("catsanddog", ["cats","dog","sand","and","cat"])
# # Solution().wordBreak("abcd", ["a","abc","b","cd"])