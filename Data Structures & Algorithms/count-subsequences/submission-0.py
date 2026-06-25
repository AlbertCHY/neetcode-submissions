class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0

        memo = {}
        
        def dfs(i, j):
            if j == n:
                return 1
            if i == m:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if s[i] != t[j]:
                memo[(i, j)] = dfs(i + 1, j)
            else:
                memo[(i, j)] = dfs(i + 1, j) + dfs(i + 1, j + 1)

            return memo[(i, j)]

        return dfs(0, 0)

        