class Solution:
    def maxWidthRamp(self, nums: list[int]) -> int:
        stack = []
        longest = 0
        for i in range(len(nums) - 1, -1, -1):
            if not stack or nums[i] > nums[stack[-1]]:
                stack.append(i)
            
        
        for i in range(len(nums)):
            while stack and nums[i] <= nums[stack[-1]]:
                j = stack.pop()
                longest = max(longest, j - i)
        
        return longest
            
            