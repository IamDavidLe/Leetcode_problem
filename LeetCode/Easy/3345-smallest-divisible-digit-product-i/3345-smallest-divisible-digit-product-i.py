class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        for i in range(n, n + 10):
            prod = 1
            tmp = i
            while tmp > 0:
                num = tmp % 10
                prod *= num
                tmp = tmp // 10
            if prod % t == 0:
                return i