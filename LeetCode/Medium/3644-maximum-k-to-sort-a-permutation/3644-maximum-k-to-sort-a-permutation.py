class Solution:
    def sortPermutation(self, nums: list[int]) -> int:
        k = -1

        for i, num in enumerate(nums):
            if i != num:
                if k == -1:
                    k = num
                else:
                    k &= num

        return 0 if k == -1 else k