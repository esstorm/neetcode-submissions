class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        max_profit = 0

        while r < len(prices):
            profit = prices[r] - prices[l]
            max_profit = max(profit, max_profit)

            if prices[l] < prices[r]:
                r += 1
            else:
                l = r
                r += 1

        return max_profit


