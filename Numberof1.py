"""
二进制中1的个数

题目描述：
	输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

思路：正负整数分开，负数是用补码表示的
	 bin(n) 表示把n变成二进制字符串
	 replace('0b','') 将'0b'替换为空，二进制以0b开始，
	 计数1没有影响，若计数0则要将其去掉。
	 count()用于统计字符串里某个字符出现的次数
"""
class Solution:
	def NumberOf1(self,n):
		if n >= 0:
			return bin(n).replace('0b','').count('1')
		else:
			return bin(2**32+n).replace('0b','').count('1')
