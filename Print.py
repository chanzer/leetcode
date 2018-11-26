"""
按之字形顺序打印二叉树

题目描述：
	请实现一个函数按照之字形打印二叉树，即第一行按照从左到右的顺序打
	印，第二层按照从右至左的顺序打印，第三行按照从左到右的顺序打印，
	以此类推。

"""
class Solution:
	def Print(self,pRoot):
		if not pRoot:
			return []
		nodeStack = [pRoot]
		result = []
		while nodeStack:
			res = []
			nextStack = []
			for i in nodeStack:
				res.append(i.val)
				if i.left:
					nextStack.append(i.left)
				if i.right:
					nextStack.append(i.right)
			nodeStack = nextStack
			result.append(res)
		returnResult = []
		for i,v in enumerate(result):
			if i%2 == 0:
				returnResult.append(v)
			else:
				returnResult.append(v[::-1])
		return returnResult
