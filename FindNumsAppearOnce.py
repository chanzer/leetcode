"""
数组中只出现一次的数字

题目描述：
	一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出
	这两个只出现一次的数字。

"""
class Solution:
	def FindNumsAppearOnce(self,array):
		hashMap = {}
		for i in array:
			if i in hashMap:
				hashMap[i] += 1
			else:
				hashMap[i] = 1
		res = []
		for k in hashMap.keys():
			if hashMap[k] == 1:
				res.append(k)
		return res
