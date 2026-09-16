class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for _ in range(numRows - 1):
            temp = [0] + res[-1] + [0]
            level = []
            for j in range(len(res[-1]) + 1):
                level.append(temp[j] + temp[j+1])
            
            res.append(level)

        return res
