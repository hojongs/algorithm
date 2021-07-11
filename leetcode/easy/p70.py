"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/submissions/

DP
Discrete mathematics 강의의 기억 (점화식)
"""


class Solution:
    dp = [0] * 46  # n <= 45

    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2  # 1 + 1 or 2
        elif self.dp[n] != 0:
            return self.dp[n]

        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]
