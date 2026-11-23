class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x : (x[0], -x[1]))
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] < intervals[i][1]:
                res.append(intervals[i])
        
        return len(res)
