class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        result = 0
        while queue:
            i, j, steps = queue.popleft()
            result = max(result, steps)
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if m > ni >= 0 and n > nj >= 0 and grid[ni][nj] == 1:
                    grid[ni][nj] = 2
                    queue.append((ni, nj, steps + 1))
                    

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return result