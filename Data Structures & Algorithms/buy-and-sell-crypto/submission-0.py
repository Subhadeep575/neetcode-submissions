class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = prices[0]
        for price in prices:
            # minimum price update
            if(price < minPrice ):
                minPrice = price
            # current profit calculate
            currentProfit = price - minPrice

            # maximum profit update
            if(currentProfit > maxProfit):
                maxProfit = currentProfit
        return maxProfit