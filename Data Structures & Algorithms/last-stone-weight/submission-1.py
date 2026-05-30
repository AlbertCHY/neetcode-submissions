class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            curr1 = heapq.heappop_max(stones)
            curr2 = heapq.heappop_max(stones)
            heapq.heappush_max(stones, abs(curr1 - curr2))

        return stones[0] if stones else 0