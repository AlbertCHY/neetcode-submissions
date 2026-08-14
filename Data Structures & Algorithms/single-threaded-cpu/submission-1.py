class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort()
        heap = []
        time = tasks[0][0]
        idx = 0
        result = []

        while heap or idx < len(tasks):
            while idx < len(tasks) and time >= tasks[idx][0]:
                heapq.heappush(heap, (tasks[idx][1], tasks[idx][2]))
                idx += 1
            if not heap:
                time = tasks[idx][0]
            else:
                curr = heapq.heappop(heap)
                time += curr[0]
                result.append(curr[1])

        return result

