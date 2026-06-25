class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, m + 1):
            tmp = [0] * (n + 1)
            tmp[0] = 1
            for j in range(1, n + 1):
                if s[i - 1] != t[j - 1]:
                    tmp[j] = dp[j]
                else:
                    tmp[j] = dp[j] + dp[j - 1]
            dp = tmp

        return dp[n]

        