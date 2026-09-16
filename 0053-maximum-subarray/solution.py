class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1] + nums[i] < nums[i]:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i-1] + nums[i]
        
            largest = max(largest, dp[i])
        
        return largest