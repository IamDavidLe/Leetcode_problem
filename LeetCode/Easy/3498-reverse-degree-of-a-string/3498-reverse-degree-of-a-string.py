class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i, value in enumerate(s):
            res += (26 - (ord(value) - ord('a'))) * (i + 1)
        
        return res