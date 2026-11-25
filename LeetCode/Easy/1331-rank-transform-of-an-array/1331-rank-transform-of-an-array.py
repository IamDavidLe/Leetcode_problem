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
        
        for i in range(len(arr)):
            arr[i] = rank[arr[i]]
        
        return arr