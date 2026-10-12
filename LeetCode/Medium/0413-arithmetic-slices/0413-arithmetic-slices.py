class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        ans = 0
        dp = [0] * n
        if n < 3:
            return 0

        for i in range(2, n):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]: 
                # check if they have the same common difference
                dp[i] = dp[i-1] + 1 
                # If they do, all the previous number will have the same common difference
            ans += dp[i]
        
        return ans