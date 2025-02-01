from typing import List

class Solution:
    @staticmethod
    def my_hash(s):
        base = 7919
        primes = [1,2,3,5,7,11,13,17,19,23,29,31]
        hash = 0
        freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for c in s:
            freq[(ord(c) - ord('a') + 1)] += 1
        for c in s:
            hash += ((ord(c) - ord('a')) ** 11 + 1) * (base ** freq[(ord(c) - ord('a') + 1)] * primes[ord(c) % len(primes)])
        return hash

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hashes = {}
        for s in strs:
            hashed_val = self.my_hash(s)
            if hashed_val in hashes:
                hashes[hashed_val].append(s)
            else:
                hashes[hashed_val] = [s]
        return [arr[1] for arr in hashes.items()]

s = Solution()

# strs = ["eat","tea","tan","ate","nat","bat"]
# ans = s.groupAnagrams(strs)
# expected = [["bat"],["nat","tan"],["ate","eat","tea"]]
# assert sorted(list(map(lambda x: sorted(x), ans))) == sorted(list(map(lambda x: sorted(x), expected)))
# print(f'{strs}\t-> {sorted(ans)}')

# strs = [""]
# ans = s.groupAnagrams(strs)
# expected = [[""]]
# assert sorted(list(map(lambda x: sorted(x), ans))) == sorted(list(map(lambda x: sorted(x), expected)))
# print(f'{strs}\t-> {sorted(ans)}')

print(Solution.my_hash('and'))
print(Solution.my_hash('ace'))

strs = ["cat","rye","aye","cud","cat","old","fop","bra"]
ans = s.groupAnagrams(strs)
expected = [["bra"],["old"],["cud"],["aye"],["rye"],["fop"],["cat","cat"]]
print(f'{strs}\t-> {sorted(ans)}')
assert sorted(list(map(lambda x: sorted(x), ans))) == sorted(list(map(lambda x: sorted(x), expected)))

# # strs = ["cat","rye","aye","cud","cat","old","fop","bra"]
# # ans = s.groupAnagrams(strs)
# # print(f'ans={ans}')
