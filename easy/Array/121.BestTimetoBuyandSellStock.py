'''
121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
''' 

'''
trick: as long as the accumulated profit is not negative keep adding. while keep track of the peak so far
'''
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        curprof = 0
        maxprof = 0
        for i in range(1, len(prices)):
            curprof = max(0, curprof + prices[i] - prices[i-1])
            maxprof = max(maxprof, curprof)
        return maxprof