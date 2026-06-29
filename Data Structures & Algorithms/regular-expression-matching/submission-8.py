class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True
        
        for i in range(2, n + 1, 2):
            dp[i][0] = p[i - 1] == "*" and dp[i - 2][0]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if p[i - 1] != "*":
                    dp[i][j] = dp[i - 1][j - 1] and (s[j - 1] == p[i - 1] or p[i - 1] == ".")
                else:
                    norepeat = dp[i - 2][j]
                    repeat = (s[j - 1] == p[i - 2] or p[i - 2] == ".") and dp[i][j - 1]
                    dp[i][j] = norepeat or repeat


        return dp[n][m]
        