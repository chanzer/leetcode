"""
把字符串转换成整数

题目描述：
		将一个字符串转换成一个整数(实现Integer.valueOf(string)的功能，
		但是string不符合数字要求时返回0)，要求不能使用字符串转换整数的
		库函数。 数值为0或者字符串不是一个合法的数值则返回0。
输入描述：
		输入一个字符串，包括数字字母符号，可以为空
输出描述：
		如果是合法的数值表达则返回该数字，否则返回0
示例：
	输入： +123456789
		1a22
	输出：123456789
		0
"""
class Solution:
	def StrToInt(self,s):
		#先排除异常特殊情况
		if s in ['','-','+','+-','-+']:
			return 0
		count = 0
		#只要有非法字符就不过
		for i in s:
			#检查字母
			if i not in '0123456789+-':
				count += 1
		if count:
			return 0
		return int(s)
