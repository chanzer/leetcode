"""
二叉搜索树的第K个结点

题目描述：
	给定一颗二叉搜索树，请找出其中的第k小的结点。
	例如(5,3,7,2,4,6,8)中按结点数值大小顺序第三小的结点值为4

注意：
	二叉搜索树中序遍历就排好序的序列
	返回的是节点，不是节点的值
"""
class Solution:
	def KthNode(self,pRoot,k):
		self.res = []
		self.dfs(pRoot)
		return self.res[k-1] if 0 < k <=len(self.res) else None

	def dfs(self,root):
		if not root:
			return
		self.dfs(root.left)
		self.res.append(root)
		self.dfs(root.right)
