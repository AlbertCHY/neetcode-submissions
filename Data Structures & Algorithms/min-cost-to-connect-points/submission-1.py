class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        visited = set()
        result = 0
        heap = []

        heapq.heappush(heap, (0, 0))
        while heap:
            dist, idx = heapq.heappop(heap)
            if idx in visited:
                continue
            visited.add(idx)
            result += dist
            if len(visited) == len(points):
                break
            for i in range(len(points)):
                if i == idx:
                    continue
                if i in visited:
                    continue
                dist = abs(points[i][0] - points[idx][0]) + abs(points[i][1] - points[idx][1])
                heapq.heappush(heap, (dist, i))
            
        
        return result