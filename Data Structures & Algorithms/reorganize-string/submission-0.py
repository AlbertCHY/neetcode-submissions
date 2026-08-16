class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [[cnt, c] for c, cnt in count.items()]
        heapq.heapify_max(heap)

        prev = None
        result = ""
        while heap or prev:
            if prev and not heap:
                return ""

            cnt, c = heapq.heappop_max(heap)
            result += c
            cnt -= 1

            if prev:
                heapq.heappush_max(heap, prev)
                prev = None
            
            if cnt != 0:
                prev = [cnt, c]

        return result