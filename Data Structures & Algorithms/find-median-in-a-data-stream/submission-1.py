class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []
        self.counter = 0

    def addNum(self, num: int) -> None:
        self.counter += 1
        if self.counter % 2 == 0 or self.counter == 1:
            heapq.heappush(self.min_heap, num)
            heapq.heappush_max(self.max_heap, num)
            if self.counter != 1:
                heapq.heappop(self.min_heap)
                heapq.heappop_max(self.max_heap)
        else:
            largeSide = self.min_heap[0]
            if num >= largeSide:
                heapq.heappush(self.min_heap, num)
                heapq.heappush_max(self.max_heap, self.min_heap[0])
            else:
                heapq.heappush_max(self.max_heap, num)
                heapq.heappush(self.min_heap, self.max_heap[0])
        
            

    def findMedian(self) -> float:
        return (self.min_heap[0] + self.max_heap[0]) / 2
        