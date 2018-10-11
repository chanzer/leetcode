"""
二维数组中的查找

题目描述：
	在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右
	递增的顺序排序，每个一列都按照从上到下递增的顺序排序。请完成一个
	函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""
class Solution:
	"""array 二维列表"""
	def Find(self, target,array):
		n = len(array)
		flag = 'false'
		for i in range(n):
			if target in array[i]:
				flag = 'true'
				break
		return flag

while True:
	try:
		s = Solution()
		L = list(eval(input()))
		array = L[1]
		target = L[0]
		print (s.Find(target,array))
	except:
		break

