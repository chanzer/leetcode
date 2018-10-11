"""
字符串的排列

题目描述：
	输入一个字符串，按字典序打印出该字符串中字符的所有排列。例如输入字符串
	abd,则打印出由字符a,b,c所能排列出来的所有字符串
	abc,acb,bac,bca,cab和cba.

思路：

"""
import itertools

class Solution:
	def Permutation(self,ss):
		result = []
		if not ss:
			result []
		else:
			#itertools.permutation()  返回对象全排列的iterators(迭代器)
			#						  使用时用list()转换即可
			res = itertools.permutation(ss)
			for i in res:
				if ''.join(i) not in result:
					result.append(''.join(i))
		return  result
