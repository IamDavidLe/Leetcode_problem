class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums = set(nums)
        for i in range(max(nums) + 1):
            if i not in nums:
                return i
        
        return i + 1