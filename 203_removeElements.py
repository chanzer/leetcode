"""
Remove Linked List Elements
题目描述：
	Remove all elements from a linked list of integers
that have value val.

Example:
	Input:  1->2->6->3->4->5->6, val = 6
	Output: 1->2->3->4->5
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def removeElements(self,head,val):
		"""
		:type head:ListNode
		:type val : int
		:rtype : ListNode
		"""
		while head is not None and head.val == val:
			head = head.next

		current = head
		while current is not None:
			if current.next is not None and current.next.val == val:
				current.next = current.next.next
			else:
				current = current.next
		return head
