"""
对称得二叉树

题目描述：
	请实现一个函数，用来判断一颗二叉树是不是对称得。注意，如果一个
	二叉树同此二叉树的镜像事同样的，定义其为对称的。

"""
class Solution:
	def isSymmetrical(self,pRoot):
		if not pRoot:
			return True
		return self.compare(pRoot.left,pRoot.right)

	def compare(self,pRoot1,pRoot2):
		if not pRoot1 and not pRoot2:
			return True
		if not pRoot1 or not pRoot2:
			return False
		if pRoot1.val ==pRoot2.val:
			if self.compare(pRoot1.left,pRoot2.right) and self.compare(pRoot1.right,pRoot2.left):
				return True
		return False

