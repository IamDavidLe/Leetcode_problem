class Solution:
    def firstUniqChar(self, s: str) -> int:
        occur = {}
        for i, c in enumerate(s):
            if c not in occur:
                occur[c] = [i, 1]
            else:
                occur[c][1] += 1
            
        for info in occur.values():
            if info[1] == 1:
                return info[0]
        
        return -1