class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = []
        visited = set()
        path = []
        n = len(grid)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        result = 0

        heapq.heappush(heap, (grid[0][0], 0, 0))
        while heap:
            level, i, j = heapq.heappop(heap)
            visited.add((i, j))
            result = max(result, level)
            if i == j == n-1:
                break
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                    heapq.heappush(heap, (grid[ni][nj], ni, nj))

        return result