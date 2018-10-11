"""
合并两个排序的链表
题目描述：
	输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要
	合成后的链表满足单调不减规则

思路：比较两个链表的首结点，哪个小的结点则合并到第三个链表尾节点，并
	 向前移动一个结点。
	 步骤一结果会有一个链表先遍历结束，或者没有
	 第三个链表尾结点指向剩余未遍历结束的链表
	 返回第三个链表首结点

"""
# 方法一：
class Solution:
	def Merge(self,pHead1,pHead2):
		res = []
		while pHead1:
			res.append(pHead1.val)
			pHead1 = pHead1.next
		while pHead2:
			res.append(pHead2.val)
			pHead2 = pHead2.next
		res.sort()
		#创建一个链表，头节点是0
		dummy = ListNode(0)
		pre = dummy
		for  i in res:
			node = ListNode[i]
			pre.next = node
			pre = pre.next
		return dummy.next


# 方法二：
class Solution:
	def Merge(self,pHead1,pHead2):
		dummy = ListNode(0)
		pHead = dummy

		while pHead1 and pHead2:
			if pHead1.val >= pHead2.val:
				dummy.next = pHead2
				pHead2 = pHead2.next
			else:
				dummy.next = pHead1
				pHead1 = pHead1.next

			dummy = dummy.next

		if pHead1:
			dummy.next = pHead1
		elif pHead2:
			dummy.next = pHead2

		return pHead.next
