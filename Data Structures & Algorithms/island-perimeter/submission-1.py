class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def bfs(i, j):
            queue = deque([(i, j)])
            visited.add((i, j))
            result = 0

            while queue:
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if (nx < 0 or nx == m or ny < 0 or ny == n or grid[nx][ny] == 0):
                        result += 1
                    elif (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            return result

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return bfs(i, j)

        return 0