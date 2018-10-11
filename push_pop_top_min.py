"""
包含min函数的栈

题目描述：
	定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素
	的min函数(时间复杂度因为O(1)).

"""
class Solution:
	def __init__(self):
		self.arr = []
	def push(self,node):
		self.arr.append(node)
	def pop(self):
		return self.arr.pop()
	def top(self):
		return self.arr[-1]
	def min(self):
		return min(self.arr)
