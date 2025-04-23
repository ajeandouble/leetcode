class Solution:
    def climbStairs(self, steps: int) -> int:
        if steps == 1:
            return 1
        dp = [None for _ in range(steps)]
        dp[0] = 1   # 1st step -> 1 step
        dp[1] = 2   # 2nd step -> (1 step + 1 step) || (2 steps)

        for i in range(2, steps):
            # We can do as many "one step moves" that there are paths to reach the previous step
            # We can also do as many "two step moves" as there are paths to reach the step before the previous one
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[-1]
    
assert Solution().climbStairs(1) == 1
assert Solution().climbStairs(2) == 2
assert Solution().climbStairs(3) == 3
assert Solution().climbStairs(4) == 5
assert Solution().climbStairs(5) == 8
assert Solution().climbStairs(6) == 13
assert Solution().climbStairs(7) == 21
assert Solution().climbStairs(8) == 34
assert Solution().climbStairs(9) == 55
assert Solution().climbStairs(10) == 89
assert Solution().climbStairs(11) == 144
assert Solution().climbStairs(12) == 233
assert Solution().climbStairs(13) == 377
assert Solution().climbStairs(14) == 610
assert Solution().climbStairs(15) == 987
assert Solution().climbStairs(16) == 1597
assert Solution().climbStairs(17) == 2584
assert Solution().climbStairs(18) == 4181
assert Solution().climbStairs(19) == 6765
assert Solution().climbStairs(20) == 10946
assert Solution().climbStairs(21) == 17711
assert Solution().climbStairs(22) == 28657
assert Solution().climbStairs(23) == 46368
assert Solution().climbStairs(24) == 75025
assert Solution().climbStairs(25) == 121393
assert Solution().climbStairs(26) == 196418
assert Solution().climbStairs(27) == 317811
assert Solution().climbStairs(28) == 514229
assert Solution().climbStairs(29) == 832040
assert Solution().climbStairs(30) == 1346269
assert Solution().climbStairs(31) == 2178309
assert Solution().climbStairs(32) == 3524578
assert Solution().climbStairs(33) == 5702887
assert Solution().climbStairs(34) == 9227465
assert Solution().climbStairs(35) == 14930352
assert Solution().climbStairs(36) == 24157817
assert Solution().climbStairs(37) == 39088169
assert Solution().climbStairs(38) == 63245986
assert Solution().climbStairs(39) == 102334155
assert Solution().climbStairs(40) == 165580141