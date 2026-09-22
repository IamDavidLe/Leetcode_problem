class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        dividend1 = abs(dividend)
        divisor1 = abs(divisor)

        count = 0

        while dividend1 >= divisor1:
            temp = divisor1
            multiple = 1

            while dividend1 >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dividend1 -= temp
            count += multiple

        if (dividend < 0) != (divisor < 0):
            count = -count

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        return min(max(count, INT_MIN), INT_MAX)