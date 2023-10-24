class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = prices[0]    #set the minimum price to the first price
        profit = 0              

        #iterating through the prices once
        for price in prices:
            minPrice = min(price, minPrice)         #tracks the minimum current price seen
            profit = max(profit, price - minPrice)  #tracks the maximum avalible

        return profit   #return maximum profit seen
        
