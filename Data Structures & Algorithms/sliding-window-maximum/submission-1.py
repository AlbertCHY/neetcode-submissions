class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []
        for i in range(k):
            heapq.heappush(heap, (-nums[i], i))
        result.append(-heap[0][0])

        for j in range(k, len(nums)):
            if nums[j - k] == -heap[0][0]:
                while heap and heap[0][1] not in range(j - k + 1, j):
                    heapq.heappop(heap)
            heapq.heappush(heap, (-nums[j], j))
            result.append(-heap[0][0])
            

        return result