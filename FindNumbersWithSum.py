"""
和为S的两个数字

题目描述：
	输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正
	好是S，如果有多对数字的和等于S，输出两个数的乘积最小的。

思路：通常的想法是先找到满足条件的数组对，然后比较他们的乘积取乘积最小的
	 一组，所以数组必须要遍历完，可是我们通过数学公式推导发现，按第一数
	 从小到大的排序，第一组的乘积一定最小。
"""
class Solution:
	def FindNumbersWithSum(self,array,tsum):
		ls = []
		if not isinstance(array,list):
			return ls
		for i,v in enumerate(array):
			for v1 in array[i:]:
				if (v+v1) == tsum:
					ls.append([v,v1])
		if ls :
			return ls[0]
		else:
			return ls

