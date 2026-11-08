class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        dp = {}
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i + 1, buying) # Not buying or selling 
            if buying:
                buy = dfs(i + 1, not buying) - prices[i] # After selling you will only have one option is selling
                dp[(i, buying)] = max(buy, cooldown)
            
            if not buying:
                sell = dfs(i + 2, not buying) + prices[i] # Making profit and have to wait for cooldown
                dp[(i, buying)] = max(sell, cooldown)

            return dp[(i, buying)]
        
        return dfs(0, True)