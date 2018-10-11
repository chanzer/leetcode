"""
青蛙跳台阶

题目描述：
	一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级
	的台阶总共有多少种跳法(先后次序不同算不同的结果)

思路：  	n=1,	1
	    n=2,	2
	    n=3,	3
	    n=4,	5     本质上是斐波那契数列
"""
class Solution:
	def jumpFloor(self,number):
		res = [1,1,2]
		while  len(res)<= number:
			res.append(res[-1]+res[-2])
		return res[number]
