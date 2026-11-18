class Solution:
    def shortestToChar(self, s: str, c: str) -> list[int]:
        l, r = 0, 0 
        res = []
        prev = None
        while r < len(s):
            if s[r] == c:
                while l <= r:
                    distance = r - l
                    if prev is not None:
                        distance = min(distance, abs(prev - l))
                    
                    res.append(distance)
                    l += 1
                
                prev = r

            r += 1
        
        while l < len(s):
            res.append(abs(prev - l))
            l += 1
        
        return res
                
                        
