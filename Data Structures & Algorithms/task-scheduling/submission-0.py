class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = [0] * 26
        for t in tasks:
            freq[ord(t) - ord("A")] += 1
        
        heap = []
        for f in freq:
            if f != 0:
                heapq.heappush_max(heap, f)
        
        result = 0
        while heap:
            tmp = []
            for i in range(n + 1):
                if heap:
                    tmp.append(heapq.heappop_max(heap))
            for i in range(len(tmp)):
                if tmp[i] - 1 != 0:
                    heapq.heappush_max(heap, tmp[i] - 1)
            if heap:
                result += n + 1
            else:
                result += len(tmp)
        
        return result