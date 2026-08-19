class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        pair = []
        for i in range(n):
            pair.append((profits[i], capital[i]))
        pair.sort(key = lambda x: x[1])

        heap = []
        idx = 0
        while k > 0:
            while idx < n and pair[idx][1] <= w:
                heapq.heappush_max(heap, pair[idx])
                idx += 1
            if not heap:
                break
            gain, request = heapq.heappop_max(heap)
            w += gain
            k -= 1

        return w
            