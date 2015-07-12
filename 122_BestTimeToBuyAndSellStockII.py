class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        maxValue = 0
        for i in range(1, len(prices)):
            value = prices[i] - prices[i-1]
            if value > 0:
                maxValue += value
        return maxValue

