class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        memo = {}

        def dfs(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            tmp = 1
            if i + 1 < m and matrix[i][j] < matrix[i + 1][j]:
                tmp = max(tmp, 1 + dfs(i + 1, j ))
            if i - 1 >= 0 and matrix[i][j] < matrix[i - 1][j]:
                tmp = max(tmp, 1 + dfs(i - 1, j ))
            if j + 1 < n and matrix[i][j] < matrix[i][j + 1]:
                tmp = max(tmp, 1 + dfs(i, j + 1))
            if j - 1 >= 0 and matrix[i][j] < matrix[i][j - 1]:
                tmp = max(tmp, 1 + dfs(i, j - 1))
            memo[(i, j)] = tmp    
            return tmp

        result = 0
        for i in range(m):
            for j in range(n):
                result = max(result, dfs(i, j))

        return result
