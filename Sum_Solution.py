"""
求1+2+3+4+...+n

题目描述：
		求1+2+3+4+...+n，要求不能使用乘除法for while if else switch
		case等关键字及条件判断语句(A?B:C)
"""
class Solution:
	def Sum_Solution(self,n):
		return sum(list(range(1,n+1)))
