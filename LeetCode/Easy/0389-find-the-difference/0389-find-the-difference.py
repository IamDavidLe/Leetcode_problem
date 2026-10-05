class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = {}
        for c in s:
            count[c] = 1 + count.get(c, 0)
        
        for c1 in t:
            if c1 in count:
                count[c1] -= 1
                if count[c1] == 0:
                    del count[c1]
            
            else:
                return c1