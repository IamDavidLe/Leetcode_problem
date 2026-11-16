class Solution:
    def checkDivisibility(self, n: int) -> bool:
        total, product = 0, 1
        tmp = n
        while tmp > 0:
            num = tmp % 10 
            total += num
            product *= num
            tmp = tmp // 10
        
        return True if n % (total + product) == 0 else False
