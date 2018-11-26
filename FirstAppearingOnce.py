"""
字符流中第一个不重复的字符

题目描述：
		请实现一个函数用来找出字符流中第一个只出现一次的字符。例如，
		当从字符流中只读出前两个字符"go"时，第一个只出现一次的字符是"g"。
		当从该字符流中读出前六个字符“google"时，
		第一个只出现一次的字符是"l"。
		如果当前字符流没有存在出现一次的字符，返回#字符。
备注：
filter(function, iterable)
		function---判断函数
		iterable---可迭代对象
		返回迭代器对象
"""
class Solution:
	def __init__(self):
		self.s =''
	def FirstAppearingOnce(self):
		res = list(filter(lambda c:self.s.count(c) == 1,self.s))
		return res[0]  if res else '#'

	def Insert(self,char):
		self.s += char
