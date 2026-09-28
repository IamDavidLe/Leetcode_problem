class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        res = 0
        for i in s:
            if i  == '(':
                count += 1
                res = max(res, count)
            
            elif i == ')':
                count -= 1
        
        return res