"""
数据流中的中位数

题目描述：
		如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，
		那么中位数就是所有数值排序之后位于中间的数值。如果从数据流中
		读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的
		平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法
		获取当前读取数据的中位数。
"""
class Solution:
	def __init__(self):
		self.arr = []

	def Insert(self,num):
		self.arr.append(num)
		self.arr.sort()

	def GetMedian(self,s):
		length = len(self.arr)
		if length %2 == 1:
			return self.arr[length//2]
		return (self.arr[length//2]+self.arr[length//2-1])/2.0