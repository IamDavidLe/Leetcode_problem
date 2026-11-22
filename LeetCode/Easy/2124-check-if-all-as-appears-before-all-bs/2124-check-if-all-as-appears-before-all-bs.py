class Solution:
    def checkString(self, s: str) -> bool:
        count = {'a': 0, 'b': 0}
        for c in s:
            count[c] = 1 + count.get(c, 0)
        

        for c in s:
            if c == 'a':
                count[c] -= 1
            
            if count['a'] == 0:
                return True 

            elif c == 'b' and count['a'] != 0:
                return False
        

            
            