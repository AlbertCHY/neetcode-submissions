class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def bfs(i, j):
            queue = deque()
            queue.append((i, j, 0))
            visited = set()
            while queue:
                curr = queue.popleft()
                grid[curr[0]][curr[1]] = min(grid[curr[0]][curr[1]], curr[2])
                for k in directions:
                    next_i = curr[0] + k[0]
                    next_j = curr[1] + k[1]
                    if m > next_i >= 0 and n > next_j >= 0 and grid[next_i][next_j] != -1 and (next_i, next_j) not in visited:
                        queue.append((next_i, next_j, curr[2] + 1))
                        visited.add((next_i, next_j))


        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    bfs(i, j)


        