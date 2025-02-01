class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        if len(answerKey) == 1:
            return 1

        def algo(answerKey, k, c):
            start = 0
            end = 0
            d = 1 if answerKey[0] == c else 0
            while end < len(answerKey):
                while k >= 0 and end < len(answerKey):
                    if answerKey[end] != c:
                        k -= 1
                        if k == -1:
                            break
                    d = max(d, end-start+1)
                    end += 1

                while end < len(answerKey) and start <= end:
                    if answerKey[start] != c:
                        k = 0
                        start += 1
                        break
                    start += 1
                end += 1
            return d
        return max(algo(answerKey, k, 'F'), algo(answerKey, k, 'T'))



s = Solution()
assert s.maxConsecutiveAnswers('FFFFTFFT', 1) == 7
assert s.maxConsecutiveAnswers('FFFTTFTTFT', 3) == 8 # expected 7




assert s.maxConsecutiveAnswers('TFFT', 1) == 3
assert s.maxConsecutiveAnswers('TTFF', 2) == 4
assert s.maxConsecutiveAnswers('FFFTTFTT', 2) == 6
assert s.maxConsecutiveAnswers('TTTTTTTTTT', 1) == 10
assert s.maxConsecutiveAnswers('FFFTTFTTFT', 3) == 8
assert s.maxConsecutiveAnswers('TTFTTTTTFT', 1) == 8
