class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l = 0 
        for i in range(1,len(prices)):
            maxProfit = max(maxProfit, prices[i]-prices[l])
            if prices[i] < prices[l]:
                l = i 
        return maxProfit