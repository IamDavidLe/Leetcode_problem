class Solution:
    def myAtoi(self, s: str) -> int:
        range_pos = 2**31 - 1
        range_neg = -2**31

        res = 0
        sign = 1
        started = False

        for c in s:
            if c == ' ' and not started:
                continue

            if (c == '-' or c == '+') and not started:
                started = True

                if c == '-':
                    sign = -1

            elif c.isdigit():
                started = True
                digit = int(c)
                res = res * 10 + digit
                
                if sign * res > range_pos:
                    return range_pos
                if sign * res < range_neg:
                    return range_neg
                
            else:
                break
        if res == '' or res == '-':
            return 0

        return sign*res