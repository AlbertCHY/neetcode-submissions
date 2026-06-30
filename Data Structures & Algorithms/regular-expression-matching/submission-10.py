class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for j in range(2, n + 1, 2):
            dp[j] = p[j - 1] == "*" and dp[j - 2]

        for i in range(1, m + 1):
            record = dp[0]
            dp[0] = False
            for j in range(1, n + 1):
                tmp = dp[j]
                if p[j - 1] != "*":
                    dp[j] = record and (s[i - 1] == p[j - 1] or p[j - 1] == ".")
                else:
                    norepeat = dp[j - 2]
                    repeat = (s[i - 1] == p[j - 2] or p[j - 2] == ".") and dp[j]
                    dp[j] = norepeat or repeat
                record = tmp

        return dp[n]
        