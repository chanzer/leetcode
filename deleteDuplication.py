"""
删除链表中重复的结点

题目描述：
		在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，
		重复的结点不保留，返回链表头指针。
		例如：链表1->2->3->3->4->4->5处理后为1->2->5.
思路一：
	把所有节点的值放到一个列表中，在筛选出值数量为1的值、
思路二：
	递归
"""
#方法一：
class Solution:
	def deleteDuplication(self,pHead):
		res = []
		while pHead:
			res.append(pHead.val)
			pHead = pHead.next
		res = list(filter(lambda c: res.count(c) == 1,res))
		# 建立一个虚拟头节点
		dummy = ListNode(0)
		pre = dummy
		for i in res:
			node = ListNode(i)
			pre.next = node
			pre = pre.next
		return dummy.next

#方法二：
class Solution:
	def deleteDuplication(self,pHead):
		if pHead is None or pHead.next is None:
			return pHead
		head1 = pHead.next
		if head1.val != pHead.val:
			pHead.next = self.deleteDuplication(pHead.next)
		else:
			while pHead.val == head1.val and head1.next is not None:
				head1 = head1.next
			if head1.val != pHead.val:
				pHead = self.deleteDuplication(head1)
			else:
				return None
		return pHead
