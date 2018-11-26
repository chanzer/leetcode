"""
二叉搜索树的后序遍历序列

题目描述：
	输入一个整数数组，判断该数组是不是某二叉搜索树 的后序遍历的结果。如果是
	则输出Yes,否则输出No。假设输入数组的任意两个数字互不相同。
思路：
	后续遍历中，最后一个数字是树的根节点，数组中前面的数字可以分成两个部分
	第一部分的是左子树节点的值，都比根节点的值小；
	第二部分的是右子树节点的值，都比根节点的值大；
	后面用递归判断前后两部分是否符合以上原则
"""
class Solution:
	def VerifySquenceOfBST(self,sequence):
		length = len(sequence)
		if length == 0:
			return False
		if length == 1:
			return True
		root = sequence[-1]
		left = 0
		#判断左子树位置，找到临界值
		while sequence[left] < root:
			left += 1
		#右子树节点值 大于 根节点
		for i in range(left,length-1):
			if sequence[i] <root:
				return False
		return self.VerifySquenceOfBST(sequence[0:left]) or self.VerifySquenceOfBST(sequence[left:length-1])

