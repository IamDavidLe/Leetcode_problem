class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        longest = 0
        increasing = [1]  * len(nums)
        decreasing = [1] * len(nums)
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > prev:
                increasing[i] = increasing[i-1] + 1
            prev = nums[i]
        
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < prev:
                decreasing[i] = decreasing[i-1] + 1
            prev = nums[i]
        
        return max(max(increasing), max(decreasing))