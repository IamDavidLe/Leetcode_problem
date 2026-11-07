class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for num in prices:
            if num < min_price:
                min_price = num

            elif num > min_price:
                max_profit = max(max_profit, num - min_price)
        
        return max_profit