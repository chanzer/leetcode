"""
二叉搜索树与双向链表

题目描述：
	输入一颗二叉搜索树，将该二叉搜索树转换成一个排序的双向链表。要求不能
	创建任何新的结点，只能调整树中结点指针的指向。

思路：先中序遍历，将所有结点保存到一个列表中。对这个list[:-1]进行遍历，
	 每个节点的right设为下一个节点，下一个节点的left设为上一个节点。

"""
class Solution:
	def Convert(self,pRootOfTree):
		if not pRootOfTree:
			return
		self.arr = []
		self.midTraversal(pRootOfTree)
		#enumerate()  用于将一个可遍历的数据对象（如列表、元祖或字符串）
		#			组合成一个索引序列，同时列出数据和数据下标，
		#			一般用在for循环中
		for i,v in enumerate(self.arr[:-1]):
			v.right = self.arr[i+1]
			self.arr[i+1].left = v
		return self.arr[0]

	def midTraversal(self,root):
		if not root:
			return
		self.midTraversal(root.left)
		self.arr.append(root)
		self.midTraversal(root.right)
