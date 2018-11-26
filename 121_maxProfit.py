"""
Best Time to Buy and Sell Stock
题目描述：
		Say you have an array for which the ith element is
		the price of a given stock on day i.
		If you were only permitted to complete at most one
		transaction (i.e., buy one and sell one share of
		the stock), design an algorithm to find the maximum
		profit.
Note:
	Note that you cannot sell a stock before you buy one.
Example 1:
	Input:[7,1,5,3,6,4]
	Output:5
	Expalnation:Buy on day 2 (price = 1) and sell on day 5
				(price = 6), profit = 6-1 = 5.Not 7-1 = 6,
				as selling price needs to be larger than
				buying price.
Example 2:
	Input:[7,6,4,3,1]
	Output:0
	Expalnation:In this case, no transaction is done, i.e.
	 			max profit = 0.
"""
# 方法一：100ms,beat3%
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res,max_i = 0,0
        for i in reversed(prices):
        	if i > max_i:
        		max_i = i
        	res = max(max_i-i,res)
        return res
# 方法二：
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
        	return 0
        profit = 0
        buy = prices[0]
        for i in range(1,len(prices)):
        	if prices[i] < buy:
        		buy = prices[i]
        	elif profit <prices[i] - buy:
        		profit = prices[i] - buy
        return profit


