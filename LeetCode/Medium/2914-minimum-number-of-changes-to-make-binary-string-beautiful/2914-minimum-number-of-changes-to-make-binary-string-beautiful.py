class Solution:
    def minChanges(self, s: str) -> int:
        i = 0
        count = 0
        while i < len(s):
            if i != 0 and (i + 1) % 2 == 0:
                if s[i - 1:i + 1][1] != s[i - 1:i + 1][0]:
                    count += 1
            
            i += 1
                
        return count
