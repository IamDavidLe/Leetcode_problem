class Solution:
    def checkString(self, s: str) -> bool:
        res = True
        flag = False 

        for c in s:
            if c == 'b':
                flag = True
            
            if c == 'a' and flag:
                return False
        
        return True
        

            
            