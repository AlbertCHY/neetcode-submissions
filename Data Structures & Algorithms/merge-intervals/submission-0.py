class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        curr = intervals[0]
        result = []
        for i in range(len(intervals)):
            if curr[1] < intervals[i][0]:
                result.append(curr)
                curr = intervals[i]
            else:
                curr[1] = max(curr[1], intervals[i][1])

        result.append(curr)
        return result
