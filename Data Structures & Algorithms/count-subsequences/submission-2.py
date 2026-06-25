class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for j in range(m + 1):
            dp[0][j] = 1

        for i in range(1, n + 1):
            for j in range(i, m + 1):
                if s[j - 1] != t[i - 1]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

        print(dp)
        return dp[n][m]

        