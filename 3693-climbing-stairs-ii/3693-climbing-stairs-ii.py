class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [0] * (n + 1)
        
        for i in range(1, n + 1):
            dp[i] = float('inf')
            for j in range(1, min(3, i) + 1):
                dp[i] = min(dp[i], costs[i-1] + j**2 + dp[i-j])
        
        return dp[n]
        
                
