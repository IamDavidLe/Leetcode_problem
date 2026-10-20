class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = 0
        R_count = L_count = 0
        for c in s:
            if c == 'R':
                R_count += 1
            elif c == 'L':
                L_count += 1
            if R_count == L_count:
                res += 1
                R_count = 0
                L_count = 0
        
        return res