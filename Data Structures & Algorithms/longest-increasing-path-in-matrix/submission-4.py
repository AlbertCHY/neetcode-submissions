class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        memo = {}

        def dfs(i, j, prev):
            if i < 0 or i == m or j < 0 or j == n or prev >= matrix[i][j]:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            tmp = 1
            tmp = max(tmp, 1 + dfs(i + 1, j, matrix[i][j]))
            tmp = max(tmp, 1 + dfs(i - 1, j, matrix[i][j]))
            tmp = max(tmp, 1 + dfs(i, j + 1, matrix[i][j]))
            tmp = max(tmp, 1 + dfs(i, j - 1, matrix[i][j]))
            memo[(i, j)] = tmp    
            return tmp

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j, -1))

        return result
