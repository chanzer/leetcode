"""
调整数组顺序是奇数位于偶数前面

题目描述：
	输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有
	的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，并保证奇
	数和奇数，偶数和偶数之间的相对位置不变。
"""
class Solution:
	def reOrderArray(self,array):
		odd,even=[],[]
		for i in array:
			if  i%2 == 0:
				odd.append(i)
			else:
				even.append(i)
		return even+odd
