'''
122. Best Time tro Buy and Sell Stock 
say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        
        for i in range(len(prices)-1):
            profit += max(0, prices[i+1] - prices[i])
        
        return profit 
 