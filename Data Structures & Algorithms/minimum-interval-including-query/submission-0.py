class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        result = []
        n, m = len(intervals), len(queries)

        def search(target):
            l, r = 0, n
            while l < r:
                mid = (l + r) // 2
                if intervals[mid][0] <= target:
                    l = mid + 1
                else:
                    r = mid
            return l


        for i in range(m):
            l = search(queries[i])
            tmp = float("inf")
            for j in range(l):
                if intervals[j][1] < queries[i]:
                    continue
                tmp = min(tmp, intervals[j][1] - intervals[j][0] + 1)
            result.append(tmp if tmp != float("inf") else -1)

        return result