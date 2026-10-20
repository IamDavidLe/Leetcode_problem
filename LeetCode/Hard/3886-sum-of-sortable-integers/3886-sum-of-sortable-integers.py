class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)

        def can_sort(k):
            prev_max = float('-inf')

            for start in range(0, n, k):
                end = start + k
                block = nums[start:end]

                minimum = min(block)
                maximum = max(block)

                if prev_max > minimum:
                    return False

                descents = 0

                for i in range(1, k):
                    if block[i] < block[i - 1]:
                        descents += 1

                if descents > 1:
                    return False

                if descents == 1 and block[-1] > block[0]:
                    return False

                prev_max = maximum

            return True

        res = 0

        for k in range(1, n + 1):
            if n % k == 0 and can_sort(k):
                res += k

        return res