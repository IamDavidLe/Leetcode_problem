class Solution:
    def sumAndMultiply(self, n: int) -> int:
        res = []
        temp = n
        while temp > 0:
            val = temp % 10
            if val != 0 :
                res.append(val)
            temp = temp // 10

        if not res:
            return 0

        total = sum(res)
        return int(''.join(map(str, res[::-1]))) * total # join only accepts string type