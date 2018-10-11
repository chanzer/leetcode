"""
数值的整数次方

题目描述：
	给定一个double类型的浮点数base和int类型的整数exponent。
	求base的exponent次方。
"""

#方法一：（投机取巧型）
class Solution:
	def Power(self,base,exponent):
		return pow(base,exponent)

#方法二：（仔细分析型）
class Solution:
	def Power(self,base,exponent):
		flag = 0
		if base == 0:
			return False
		if exponent == 0:
			return 1
		if exponent <0 :
			flag = 1
		result = 1
		for i in range(abs(exponent)):
			result *= base
		if flag == 1:
			result = 1/result
		return result
