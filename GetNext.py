"""
二叉树的下一个结点

题目描述：
		给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点
		并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结
		点的指针
思路：
	先写一个中序遍历的算法。关键是从根节点开始遍历，所所以第一步还是找到
	某个节点的根节点，方法是一直使用next判断
	在将从根节点中序遍历的结果保存到一个数组中，直接找pNode所在索引的
	下一个即可。要考虑这个节点是不是最后一个，若是，直接返回None。

"""
class Solution:
	def GetNext(self,pNode):
		dummy = pNode
		while dummy.next:
			dummy = dummy.next
		self.result = []
		self.midTraversal(dummy)
		if self.result.index(pNode) != len(self.result)-1:
			return self.result[self.result.index(pNode)+1]
		else:
			return None

	def midTraversal(self,root):
		if not root : return None
		self.midTraversal(root.left)
		self.result.append(root)
		self.midTraversal(root.right)
