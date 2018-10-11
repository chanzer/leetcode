"""
替换空格

题目描述：
	请实现一个函数，将一个字符串中的每个空格替换成"%20"。例如：当字
	符串为 We Are Happy.则经过替换之后的字符串为We%20Are%20Happy.
"""

class Solution:
	def replaceSpace(self,s):
		i = 0
		n = len(s)
		#用于盛放转发完的字符串
		ss = []
		for i in range(n):
			#判断是否为空格位
			if s[i].isspace():
				ss.append('%20')
			else:
				ss.append(s[i])
			i +=1
		#将列表转化为字符串
		ss = ''.join(ss)
		return ss
