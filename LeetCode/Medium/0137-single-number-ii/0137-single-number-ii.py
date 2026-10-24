class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = ''

        for i in range(32):
            count = 0

            for num in nums:
                if num & (1 << i):
                    count += 1

            val = str(count % 3)
            res = val + res

        if res[0] == '1':
            return int(res, 2) - (1 << 32)

        return int(res, 2)