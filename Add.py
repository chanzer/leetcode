"""
不用加减乘除做加法

题目描述：
		写一个函数，求两数之和，要求在函数体内不得使用+ -*/四则运算符号
"""

# 猥琐流做法
class Solution:
	def Add(self,num1,num2):
		return sum([num1,num2])



#正常做法：位运算
#1.两个数异或：相当于每一位相加，而不考虑进位；
#2.两个数相与，并左移一位：相当于求得进位；
#3.将上述两步的结果相加

class Solution:
	def Add(self,num1,num2):
		while num2 != 0:
			carry = num1 & num2
			num1 = (num1 ^ num2)%0x100000000
			num2 = (carry <<1)0x100000000

		return num1 if num1 <= 0x7FFFFFFF else num1 |(~0x100000000+1)
