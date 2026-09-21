class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n] * (n + 1)
        square = set()
        i = 1
        while i ** 2 <= n:
            dp [i ** 2] = 1
            square.add(i ** 2)
            i += 1

        for i in range(1, n + 1):
            for s in square:
                dp[i] = min(dp[i], dp[i - s] + 1)
        

        return dp[n]