class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_prices = prices[0]

        for i in range (len(prices)):
            if min_prices > prices[i]:
                min_prices = prices[i]

            profit = prices[i] - min_prices
            max_profit = max(profit, max_profit)

        return max_profit

        