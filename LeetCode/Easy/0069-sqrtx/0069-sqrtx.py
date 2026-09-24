class Solution:
    def mySqrt(self, x: int) -> int:
        l, r = 0, x

        if x == 0 or x == 1:
            return x
        
        while l <= r:
            val = (l + r) // 2
            if math.floor(val * val) > x:
                r = val - 1
            elif math.floor(val * val) < x:
                l = val + 1
            else:
                return val
                
        return r