"""
数的子结构
题目描述：
	输入两棵二叉树A,B,判断B是不是A的子结构。
	空树不是任何一个数的子结构
思路：

"""
#方法一：
class Solution:
	def HasSubtree(self,pRoot1,pRoot2):
		def convert(p):
			if p:
				return str(p.val)+convert(p.left)+convert(p.right)
			else:
				return ''
		if pRoot2:
			return convert(pRoot2) in convert(pRoot1)
		else:
			return False

#方法二：
class Solution:
	def HasSubtree(self,pRoot1,pRoot2):
		if not pRoot1 or not pRoot2:
			return False
		return  self.is_subtree(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)

	def is_subtree(self,A,B):
		if not B:
			return True
		if not A or A.val != B.val:
			return False
		return self.is_subtree(A.left,B.left) and self.is_subtree(A.right,B.right)
