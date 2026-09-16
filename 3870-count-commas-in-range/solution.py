class Solution:
    def countCommas(self, n: int) -> int:
        if n >= 1000:
            return n - 999
        return 0