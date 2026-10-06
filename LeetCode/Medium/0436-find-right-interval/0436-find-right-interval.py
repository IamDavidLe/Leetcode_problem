class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)

        starts = []
        for i in range(n):
            starts.append((intervals[i][0], i))
        
        starts.sort()

        res = []

        for start, end in intervals:
            l, r = 0, n - 1
            ans = -1
            while l <= r:
                mid = (l + r) // 2
                if starts[mid][0] >= end:
                    ans = starts[mid][1]
                    r = mid - 1
                else:
                    l = mid + 1

            res.append(ans)

        return res