class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        while n not in visit:
            visit.add(n)
            n = self.sumofsquare(n)
            if n == 1:
                return True
        
        return False
    
    def sumofsquare(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n //= 10
        
        return output

