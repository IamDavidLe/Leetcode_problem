class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        copy = arr[:]
        copy.sort()
        rank = {}
        start = 1
        for num in copy:
            if num not in rank:
                rank[num] = start
                start += 1
        
        res = []
        for n in arr:
            res.append(rank[n])
        
        return res