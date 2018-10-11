"""
前序遍历重建二叉树

题目描述：
	输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设
	输入的前序遍历和中序遍历的结果中都不含重复的数字。例如输入前序
	遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6},
	则重建二叉树并返回。
"""
class Solution:
	#返回构造的TreeNode根节点
	def reConstructBinaryTree(self,pre,tin):
		if len(pre) == 0:
			return None
		#将根定义成节点的形式
		root_data = TreeNode(pre[0])
		i = tin.index(pre[0])
		#寻找位置将左右子树分开，并递归遍历
		root_data.left = self.reConstructBinaryTree(pre[1:i+1],tin[:i])
		root_data.right = self.reConstructBinaryTree(pre[i+1:],tin[i+1:])
		return root_data
