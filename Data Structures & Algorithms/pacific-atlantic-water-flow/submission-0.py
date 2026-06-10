class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        pacific, atlantic = set(), set()
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    pacific.add((i, j))
                if i == m - 1 or j == n - 1:
                    atlantic.add((i, j))

        def dfs(i, j, ocean):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            if (i, j) in visited:
                return

            ocean.add((i, j))
            visited.add((i, j))
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and heights[i][j] <= heights[ni][nj]:
                    dfs(ni, nj, ocean)

        visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) not in visited:
                    dfs(i, j, pacific)

        visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) in atlantic and (i, j) not in visited:
                    dfs(i, j, atlantic)
        
        result = []
        for i in range(m):
            for j in range(n):
                if (i, j) in pacific and (i, j) in atlantic:
                    result.append([i, j])

        return result