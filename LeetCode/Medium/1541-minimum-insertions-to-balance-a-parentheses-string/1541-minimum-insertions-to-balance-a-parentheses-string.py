class Solution:
    def minInsertions(self, s: str) -> int:
        need, res = 0, 0
        
        for bracket in s:
            if bracket == '(':
                if need % 2 == 1:
                    res += 1
                    need -= 1
                
                need += 2
            
            else:
                need -= 1

                if need == -1:
                    res += 1
                    need = 1
        
        return res + need