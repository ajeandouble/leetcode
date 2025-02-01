class Solution:
    # def has_stranger_character(self, s1, s2):
    #     for
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1freqs, s2freqs = [0] * 26, [0] * 26
        for c in s1:
            s1freqs[ord(c) - ord('a')] += 1

        l, r = 0, 0
        while r < len(s2):
            f_idx = ord(s2[r]) - ord('a')
            s2freqs[f_idx] += 1
            print(l, r, s1freqs, s2freqs)
            if s2freqs == s1freqs:
                print(s2freqs, s2[l:r+1])
                return True
            pas_cool = False
            for (i, c) in enumerate(s1freqs):
                if s2freqs[i] - s1freqs[i] > 0:
                    f_idx = ord(s2[l]) - ord('a')
                    s2freqs[f_idx] -= 1
                    l += 1
                    pas_cool = True
                    break
            print('break', pas_cool)
            r += 1
        return False


s = Solution()

s1 = "ab"
s2 = "eidbaooo"

# assert s.checkInclusion(s1, s2) == True


s1 = "ab"
s2 = "eidboaoo"

assert s.checkInclusion(s1, s2) == False
