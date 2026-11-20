class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        dp = {}

        for x in nums:
            dp[x + 1] = max(dp.get(x + 1, 0), dp.get(x, 0) + 1)

            dp[x] = max(dp.get(x, 0), dp.get(x - 1, 0) + 1)

        return max(dp.values())