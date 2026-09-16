class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        total = 0
        div = 1000
        comma = 1

        while div <= n:
            end = min(n, div * 1000 - 1)
            total += (end - div + 1) * comma

            div *= 1000
            comma += 1

        return total