class Solution:
    def reverse(self, x: int) -> int:
        range_pos, range_neg = 2**31 -1, -2**31
        if x < 0:
            a = str(-x)
            reversed_num = -int(a[::-1])
        else:
            a = str(x) 
            reversed_num = int(a[::-1])

        if reversed_num < range_neg or reversed_num > range_pos:
            return 0
        
        return reversed_num
        