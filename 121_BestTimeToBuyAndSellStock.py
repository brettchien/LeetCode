class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        maxValue = 0
        current = 0
        for i in range(1, len(prices)):
            current += prices[i] - prices[i-1]
            if current < 0:
                current = 0
            if current > maxValue:
                maxValue = current
        return maxValue

