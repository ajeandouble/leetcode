from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for s in strs:
            d["".join(sorted(s))].append(s)
        return [x for x in d.values()]


s = Solution()
input = ["eat", "tea", "tan", "ate", "nat", "bat"]
ans = s.groupAnagrams(input)
print(f"{input} => {ans}")
assert ans == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

input = [""]
ans = s.groupAnagrams(input)
print(f"{input} => {ans}")
assert ans == [[""]]

input = ["a"]
ans = s.groupAnagrams(input)
print(f"{input} => {ans}")
assert ans == [["a"]]
