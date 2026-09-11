class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        heap = [[0, 0, 0]]
        visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while heap:
            effort, r, c = heapq.heappop(heap)
            if (r, c) in visited:
                continue

            visited.add((r, c))
            if (r, c) == (m - 1, n - 1):
                return effort

            for x, y in directions:
                nr, nc = r + x, c + y
                if nr < 0 or nc < 0 or nr == m or nc == n or (nr, nc) in visited:
                    continue
                nEffort = max(effort, abs(heights[r][c] - heights[nr][nc]))
                heapq.heappush(heap, [nEffort, nr, nc])

        return 0