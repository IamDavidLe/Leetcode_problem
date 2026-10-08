class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        
        if len(s) == 0:
            return True 
        
        pointer = 0
        for i in range(len(t)):
            if s[pointer] == t[i]:
                pointer += 1
            
            if pointer == len(s):
                return True
        
        return False