from typing import List


class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        N = len(nums)
        memo = {}
        player1_score = player2_score = 0

        def dfs(l, r, player1=True):
            if l > r:
                return 0
            if l == r:
                return nums[l]
            if (l, r) in memo:
                return memo[(l, r)]
            take_left = nums[l] - dfs(l + 1, r, not player1)
            take_right = nums[r] - dfs(l, r - 1, not player1)
            # print(f"on ({l}, {r}); left == {take_left}, right == {take_right}")
            # print(f"{'player' + ('1' if player1 else '2')} takes {nums[l] if take_left >= take_right else nums[r]}")
            max_delta = max(take_left, take_right)
            memo[(l, r)] = max_delta
            if player1:
                nonlocal player1_score
                player1_score += max_delta
            else:
                nonlocal player2_score
                player2_score += max_delta
            # print(f"max_delta == {max_delta}")
            return max_delta

        return dfs(0, N - 1) >= 0
