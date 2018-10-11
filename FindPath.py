"""
二叉树中和为某一值的路径

题目描述：
	输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值得和为输入整数的
	所有路径。路径定义为从树的根节点开始往下一直到叶节点所经过的结点形成一
	条路径。（注意：返回值的list中，数组长度大的数组靠前）
思路：

"""
class Solution:
	def FindPath(self,root,expectNumber):
		if not root:
			return []
		if root and not root.left and not root.right and root.val == expectNumber:
			return[[root.val]]
		res = []
		left = self.FindPath(root.left,expectNumber-root.val)
		right = self.FindPath(root.right,expectNumber-root.val)
		for i in left+right:
			res.append([root.val]+i)
		return res
