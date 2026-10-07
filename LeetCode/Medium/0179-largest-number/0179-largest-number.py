class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        strs = list(map(str, nums))

        swapped = True

        while swapped:
            swapped = False

            for i in range(1, len(strs)):
                if strs[i - 1] + strs[i] < strs[i] + strs[i - 1]:
                    strs[i - 1], strs[i] = strs[i], strs[i - 1]
                    swapped = True

        result = ''.join(strs)

        return '0' if result[0] == '0' else result