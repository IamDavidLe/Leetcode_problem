class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        res = []
        if m*n != len(original) :
            return []
        for i in range(m):
            level = []
            for j in range(n):
                level.append(original[i * n + j])
            res.append(level)
    
        return res 
