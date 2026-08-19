class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        highestSell = prices[len(prices)-1]
        maxProfit = 0
        for i in range(len(prices) - 1,-1,-1):
            if i == len(prices)-1:
                continue
            maxProfit = max(maxProfit, highestSell - prices[i])
            highestSell = max(highestSell, prices[i])
        return maxProfit if maxProfit > 0 else 0