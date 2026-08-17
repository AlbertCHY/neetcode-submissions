class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        if a != 0:
            heapq.heappush_max(heap, [a, "a"])
        if b != 0:
            heapq.heappush_max(heap, [b, "b"])
        if c != 0:
            heapq.heappush_max(heap, [c, "c"])
        result = []

        counter = 0
        tmp = None
        while heap:
            curr = heapq.heappop_max(heap)
            if counter == 2 and curr[1] == result[-1]:
                if not heap:
                    break
                tmp = curr
                curr = heapq.heappop_max(heap)
            if not result or curr[1] != result[-1]:
                counter = 1
            else:
                counter += 1
            result.append(curr[1])
            curr[0] -= 1
            if curr[0] != 0:
                heapq.heappush_max(heap, [curr[0], curr[1]])
            if tmp:
                heapq.heappush_max(heap, tmp)
                tmp = None


        return "".join(result)