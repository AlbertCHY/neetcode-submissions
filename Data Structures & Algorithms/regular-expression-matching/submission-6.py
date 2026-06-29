class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = True
        if p[-1] == "*":
            dp[m][n - 2] = True

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if j + 1 < n:
                    nxt = p[j + 1]
                else:
                    nxt = "0"

                result = False
                if nxt != "*":
                    if p[j] == s[i] or p[j] == ".":
                        result = dp[i + 1][j + 1]
                else:
                    if p[j] == s[i] or p[j] == ".":
                        result = dp[i + 1][j] or dp[i][j + 2]
                    else:
                        result = dp[i][j + 2]
                dp[i][j] = result

        return dp[0][0]


        # def dfs(i, j):
        #     if i == m:
        #         if j >= n or j == n - 2 and p[-1] == "*":
        #             return True
        #         else:
        #             return False

        #     if j >= n:
        #         return False

        #     if (i, j) in memo:
        #         return memo[(i, j)]

        #     if j + 1 < n:
        #         nxt = p[j + 1]
        #     else:
        #         nxt = "0"

        #     result = False
        #     if nxt != "*":
        #         if p[j] == s[i] or p[j] == ".":
        #             result = dfs(i + 1, j + 1)
        #     else:
        #         if p[j] == s[i] or p[j] == ".":
        #             result = dfs(i + 1, j) or dfs(i, j + 2)
        #         else:
        #             result = dfs(i, j + 2)
        #     memo[(i, j)] = result
        #     return result

        # return dfs(0, 0)
        