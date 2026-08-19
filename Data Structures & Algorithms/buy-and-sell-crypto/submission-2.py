class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # The other one was perfectly fine but showing i can do it from the left too
        lowestBuy = prices[0]
        maxProfit = 0
        for i in range(len(prices)):
            if i == 0:
                continue
            maxProfit = max(maxProfit, prices[i] - lowestBuy)
            lowestBuy = min(lowestBuy, prices[i])
        return maxProfit if maxProfit > 0 else 0
