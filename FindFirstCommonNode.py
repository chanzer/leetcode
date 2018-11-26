"""
两个链表的第一个公共结点

题目描述：
	输入两个链表，找出它们的第一个公共结点。

"""
class Solution:
	def FindFirstCommonNode(self,pHead1,pHead2):
		list1 = []
		list2 = []
		node1 = pHead1
		node2 = pHead2
		while node1:
			list1.append(node1.val)
			node1 = node1.next
		while node2:
			if node2.val in list1:
				return node2
			else:
				node2 = node2.next
