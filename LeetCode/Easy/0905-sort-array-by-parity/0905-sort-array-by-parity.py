class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        return sorted(nums, key = lambda x: (x % 2, x))