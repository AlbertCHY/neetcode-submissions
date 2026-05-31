class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            heapq.heappush_max(heap, (math.hypot(points[i][0], points[i][1]), points[i]))
            if len(heap) > k:
                heapq.heappop_max(heap)


        return  list(x[1] for x in heap)