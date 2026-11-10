class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)
        n = len(cost)
        dp = [0] * n 
        dp[0], dp[1] = cost[0], cost[1]
        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i-1], dp[i-2])

        return dp[n-1]