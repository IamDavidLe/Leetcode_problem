class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum > 9 * num:
            return ''
        
        res = []
        for i in range(num):
            digit = min(9, sum)
            res.append(str(digit))
            sum -= digit
        
        return ''.join(res)