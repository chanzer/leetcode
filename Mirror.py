"""二叉树的镜像
题目描述：
	操作给定的二叉树，将其变换为源二叉树的镜像。
思路：根节点左右交换

"""
class Solution:
	def Mirror(self,root):
		if root != None:
			root.left,root.right = root.right,root.left
			self.Mirror(root.left)
			self.Mirror(root.right)

