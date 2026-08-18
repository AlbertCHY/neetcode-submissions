class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        onheap = []
        offheap = []
        incar = 0
        for trip in trips:
            heapq.heappush(onheap, (trip[1], trip[0]))
            heapq.heappush(offheap, (trip[2], trip[0]))

        while onheap:
            if onheap[0][0] < offheap[0][0]:
                curr = heapq.heappop(onheap)
                incar += curr[1]
                if incar > capacity:
                    return False
            else:
                curr = heapq.heappop(offheap)
                incar -= curr[1]

        return True