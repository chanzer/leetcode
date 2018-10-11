"""
矩形覆盖

题目描述：
	我们可以用2*1得小矩形横着或者竖着去覆盖更大得矩形。请问用n个2*1
	的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

思路：依旧是斐波那契数列
	  number = 0,     0
	  number = 1,     1
	  number = 2,     2
	  number > 2,    f(n) = f(n-1)+f(n-2)

"""
class Solution:
	def rectCover(self,number):
		res = [0,1,2]
		while len(res) <= number:
			res.append(res[-1]+res[-2])
		return res[number]
