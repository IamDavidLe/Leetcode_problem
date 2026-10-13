class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if (n % 2 == 1 and n != 1) or n <= 0:
            return False
        
        def power_two(n):
            if n == 1:
                return True
            
            if n % 2 == 1:
                return False
            
            return power_two(n / 2)

        return power_two(n)