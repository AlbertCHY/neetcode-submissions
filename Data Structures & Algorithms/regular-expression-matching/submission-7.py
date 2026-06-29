class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True
        i = n - 1
        while i >= 0 and p[i] == "*":
            dp[m][i - 1] = True
            i -= 2

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if j + 1 < n:
                    nxt = p[j + 1]
                else:
                    nxt = "0"

                result = False
                if nxt != "*":
                    if i < m and (p[j] == s[i] or p[j] == "."):
                        result = dp[i + 1][j + 1]
                else:
                    if i < m and (p[j] == s[i] or p[j] == "."):
                        result = dp[i + 1][j] or dp[i][j + 2]
                    else:
                        result = dp[i][j + 2]
                dp[i][j] = result

        return dp[0][0]
        