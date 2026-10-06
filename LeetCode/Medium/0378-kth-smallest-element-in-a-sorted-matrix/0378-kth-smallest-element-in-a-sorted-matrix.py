class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        tmp = []
        for l in matrix:
            tmp.extend(l)
        
        tmp.sort()
        return tmp[k-1]