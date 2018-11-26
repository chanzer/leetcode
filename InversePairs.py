"""
数组中的逆序对

题目描述：
	在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一
	个逆序对。输入一个数组，求出这个数组中的逆序对的总对数P。并将P对
	1000000007取模的结果输出。即输出P%1000000007

"""

from collections import deque
class Solution:
	def __init__(self):
		self.count = 0

	def InversePairs(self,lis):
		return self.count%1000000007

	def mergeSort(self,lis):
		if len(lis) <= 1:
			return lis
		middle = int(len(lis)//2)
		left = self.mergeSort(lis[:middle])
		right = self.mergeSort(lis[middle:])
		return self.merge(left,right)

	def merge(self,left,right):
		merged,left,right = deque(),deque(left),deque(right)
		while left and right:
			if left[0] >right[0]:
				self.count += len(left)
				merged.append(right.popleft())
			else:
				merged.append(left.popleft())
		if right:
			merged.extend(right)
		else:
			merged.extend(left)
		return merged


