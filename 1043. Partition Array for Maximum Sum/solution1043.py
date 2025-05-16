from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        ans = 0
        i = 0
        while i < N:
            curr_max = float("-inf")
            curr_k = None
            for j in range(1, k + 1):
                if i + j > N:
                    break
                max_curr = max(arr[i : i + j])
                max_next = max(arr[i + j : i + j + k]) if i + j <= N else 0
                curr_k = k if i + j + k <= N else N - (i + j)
                print(f"i={i}, j={j}, max_curr={max_curr}, max_next={max_next}")
                sum_with_j = max_curr * j + max_next * curr_k
                print(f"sum_with_j=={sum_with_j}")
                if sum_with_j >= curr_max:
                    curr_max = sum_with_j
                    curr_k = j
            ans += max_curr * curr_k
            print(ans)
            i += curr_k
        return ans


assert Solution().maxSumAfterPartitioning([1, 4, 1, 5, 7, 3, 6, 1, 9, 9, 3], 4) == 83
