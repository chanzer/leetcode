"""
反转链表
题目描述：
	输入一个链表，反转链表后，输出新链表的表头。

思路：
	pHead 始终指向要反转的结点
	last 指向反转后的首结点
	每反转一个结点，把pHead结点的下一个结点指向last，last指向pHead
	成为反转后首结点，在把pHead向前移动一个结点直至None结束
"""
class Solution:
	def ReverseList(self,pHead):
		#判断链表是否为空
		if not pHead or not pHead.next:
			return pHead
		#反转链表
		last = None
		while pHead:
			temp = pHead.next
			pHead.next = last
			last = pHead
			pHead = temp
		return last
