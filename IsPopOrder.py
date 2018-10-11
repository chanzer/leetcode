"""
栈的压入、弹出序列

题目描述：
	输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列
	是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序列
	1，2，3，4，5是某栈的压入顺序，序列5，4，3，2，1是该栈序列对应
	的一个弹出序列，当4，3，5，1，2就不可能是该栈序列的弹出序列。
	注意：两个序列的长度是相等的。

"""
class Solution:
	def IsPopOrder(self,pushV,popV):
		#stack中存入pushV中取出的数据
		stack =[]
		while popV:
			#若第一个元素相等，直接都弹出，根本不用压入stack
			if pushV and popV[0] == pushV[0]:
				popV.pop(0)
				pushV.pop(0)
			#若stack的最后一个元素与popV中的第一个元素相等，将两个元素都弹出
			elif stack and stack[-1] == popV[0]:
				stack.pop()
				popV.pop(0)
			#若pussV中有数据，压入stack
			elif pushV:
				stack.append(pushV.pop(0))
			#上面的情况都不满足，直接返回false
			else:
				return False
		return True

