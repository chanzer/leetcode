"""数字在排序数组中出现的次数

题目描述：
	统计一个数字在排序数组中出现的次数。

"""
# 方法一：
class Solution:
	def GetNumberOfK(self,data,k):
		return data.count(k)

# 方法二：
class Solution:
	def GetNumberOfK(self,data,k):
		if k not in data:
			return 0
		count = 0
		for i in range(len(data)):
			if data[i] == k:
				count +=1
		return count
