"""
Reverse Linked List
题目描述：
	Reverse a singly linked list.

Example:
	Input:  1->2->3->4->5->NULL
	Output: 5->4->3->2->1->NULL
"""
class Solution:
	def reverseList(self,head):
		"""
		:type head:ListNode
		:rtype : ListNode
		"""
		cur = head
		pre = None
		while cur:
			temp = cur.next
			cur.next = pre
			pre = cur
			cur = temp
		return pre
