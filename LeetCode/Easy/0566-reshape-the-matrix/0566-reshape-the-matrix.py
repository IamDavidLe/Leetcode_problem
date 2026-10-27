class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        res = []
        ROW = len(mat)
        COL = len(mat[0])
        if r * c != ROW * COL:
            return mat

        for i in range(r):
            level = []
            for j in range(c):
                val = i * c + j
                row = val // COL
                col = val % COL
                level.append(mat[row][col])
            res.append(level)
        
        return res
