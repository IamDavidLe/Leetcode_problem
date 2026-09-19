class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = [[1]]
        for _ in range(rowIndex + 1):
            temp = [0] + res[-1] + [0]
            level = []
            for j in range(len(res[-1]) + 1):
                level.append(temp[j] + temp[j+1])
            
            res.append(level)

        return res[rowIndex]
