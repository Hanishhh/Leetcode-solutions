class Solution:
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            else:
                maximum_profit=prices[i]-min_price
                if maximum_profit>max_profit:
                    max_profit=maximum_profit

        return max_profit