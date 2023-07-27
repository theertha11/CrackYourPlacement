class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit=0
        for i in range(len(prices)):
            for j in range(i,len(prices)):
                if prices[i] < prices[j] and prices[j]-prices[i] > profit:
                    profit = prices[j] - prices[i]
        return profit