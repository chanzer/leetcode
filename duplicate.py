"""
数组中重复的数字

题目描述：
		在一个长度位n的数组里的所有数字都在0到n-1的范围内。数组中某些数字
		是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。请
		找出数组中任意一个重复的数字。例如，若长度为7的数组
		{2,3,1,0,2,5,3}，那么对应的输出是第一个重复的数字2。

"""
class Solution:
	def duplicate(self,numbers,duplication):
		if numbers == None:
			return False
		res = []
		for i in numbers:
			if i in res:
				duplication[0] = i
				return True
			res.append(i)
		return False
