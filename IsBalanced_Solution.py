"""
平衡二叉树

题目描述：
	输入一颗二叉树，判断该二叉树是否是平衡二叉树。

思路：如果二叉树的每个节点的左子树和右子树的深度差不大于1，就是平衡二叉树
"""
class Solution:
	def IsBalanced_Solution(self,pRoot):
		if pRoot == None:
			return True
		if abs(self.TreeDepth(pRoot.left)-self.TreeDepth(pRoot.right)) > 1:
			return False
		return self.IsBalanced_Solution(pRoot.left) and self.IsBalanced_Solution(pRoot.right)

	def TreeDepth(self,pRoot):
		if pRoot == None:
			return 0
		nleft = self.TreeDepth(pRoot.left)
		nright = self.TreeDepth(pRoot.right)
		return max(nleft,nright)+1
