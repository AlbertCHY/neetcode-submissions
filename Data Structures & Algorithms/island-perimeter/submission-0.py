class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])

        def dfs(i, j):
            if i < 0 or i == m or j < 0 or j == n or grid[i][j] == 0:
                return 1

            if (i, j) in visited:
                return 0

            visited.add((i, j))
            return dfs(i, j + 1) + dfs(i, j - 1) + dfs(i + 1, j) + dfs(i - 1, j)



        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return dfs(i, j)

        return 0