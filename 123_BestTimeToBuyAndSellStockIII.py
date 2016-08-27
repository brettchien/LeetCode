class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        first = 0
        second = 0
        current = 0
        for i in range(1, len(prices)):
            current += prices[i] - prices[i-1]
            if current < 0:
                if first > second:
                    second = first
                first = 0
                current = 0
            if current > first:
                first = current
            print first, second
        return first + second

if __name__ == "__main__":
    sol = Solution()
    print sol.maxProfit([2, 4, 1])
    print sol.maxProfit([6, 1, 3, 2, 4, 7])
