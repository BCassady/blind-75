class Solution:
    def climbStairs(self, n: int, memo = {}) -> int:
        if n <= 3:
            return n
        elif n in memo:
            return memo[n]
        else:
            memo[n] = self.climbStairs(n-1, memo) + self.climbStairs(n-2, memo)
            return memo[n]