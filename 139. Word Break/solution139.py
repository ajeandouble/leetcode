from typing import List


class Solution:
    def wordBreak(self, s: str, words: List[str]) -> bool:
        N = len(s)
        visited = set()

        def helper(start_idx):
            if start_idx in visited:
                return False
            visited.add(start_idx)
            if start_idx > N:
                return False
            fillin_words = words
            fillin_words = filter(
                lambda word: start_idx + len(word) <= N
                and s[start_idx:].startswith(word),
                fillin_words,
            )
            for word in fillin_words:
                if start_idx + len(word) > N:
                    continue
                if helper(start_idx + len(word)) or start_idx + len(word) == N:
                    return True
            return False

        return helper(0)


assert Solution().wordBreak("leetcode", ["leet", "code"]) == True
assert Solution().wordBreak("applepenapple", ["apple", "pen"]) == True
assert Solution().wordBreak("catsandog", ["cats, dog, sand, and, cat"]) == False
