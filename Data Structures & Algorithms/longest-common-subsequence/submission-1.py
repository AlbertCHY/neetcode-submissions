class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[-1] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = 0

        def dfs(i, j):
            if i == m or j == n:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]


            if text1[i] == text2[j]:
                dp[i][j] =  dfs(i + 1, j + 1) + 1
            else:
                dp[i][j] = max(dfs(i + 1, j), dfs(i, j + 1))

            return dp[i][j]

        return dfs(0, 0)