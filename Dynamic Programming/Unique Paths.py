class Solution:
    def uniquePaths(self, m: int, n: int, memo = {}) -> int:
        if (m, n) in memo:
            return memo[(m, n)]
        elif (n, m) in memo:
            return  memo[(n, m)]
        
        if n == 1 or m == 1:
            memo[(m, n)] = 1
            return  memo[(m, n)]
        
        memo[(m, n)] = self.uniquePaths(m-1, n, memo) + self.uniquePaths(m, n-1, memo)
        return memo[(m, n)]