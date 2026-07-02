class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        counter = 0
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if curr[1] > intervals[i][0]:
                if curr[1] >= intervals[i][1]:
                    curr = intervals[i]
                counter += 1
            else:
                curr = intervals[i]
        
        return counter