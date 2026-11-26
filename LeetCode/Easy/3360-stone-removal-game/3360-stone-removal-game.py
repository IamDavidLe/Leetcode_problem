class Solution:
    def canAliceWin(self, n: int) -> bool:
        start = n - 10
        if start < 0:
            return False
        Alice = False
        for i in range(9, 0 , -1):
            start = start - i
            if start < 0 and Alice:
                return False
            
            elif start < 0 and not Alice:
                return True 
            
            Alice = not Alice
        
        