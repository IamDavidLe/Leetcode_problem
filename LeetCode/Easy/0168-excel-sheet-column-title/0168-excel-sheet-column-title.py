class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        n = columnNumber
        res = ''
        while n > 0:
            n -= 1
            remain = n % 26
            char = chr(ord('A') + remain)
            res += char
            n = n // 26

        return res[::-1]