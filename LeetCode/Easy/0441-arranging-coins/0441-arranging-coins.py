class Solution:
    def arrangeCoins(self, n: int) -> int:
        require = 1
        count = 0

        while n >= require:
            n -= require
            count += 1
            require += 1

        return count