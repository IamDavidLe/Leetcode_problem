class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int1 = int(a, 2)
        int2 = int(b, 2)
        res = int1 + int2
        return bin(res)[2:]