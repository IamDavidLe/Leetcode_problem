class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        c = columnTitle
        n = len(c)
        res = 0
        for i in range(n):
            num = ord(c[i]) - ord('A') + 1
            res += num * (26 ** (n - i - 1))

        return res