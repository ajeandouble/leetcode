class Solution:
    def maxProfit(self, prices) -> int:
        N = len(prices)
        l, r = 0, N - 1
        max_on_right = [0] * N
        max_so_far = float("-inf")
        max_price_diff = 0
        for i in range(N - 1, -1, -1):
            max_so_far = max(max_so_far, prices[i])
            max_on_right[i] = max_so_far
            max_price_diff = max(max_price_diff, max_so_far - prices[i])
        return max_price_diff


assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5
assert Solution().maxProfit([2, 1, 4]) == 3
