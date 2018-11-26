"""
Palindrome Linked List
题目描述：
	Given a singly linked list, determine if it is a palindrome.

Example 1:
	Input:  1->2
	Output: false

Example 2:
	Input:  1->2->2->1
	Output: true
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
	def isPalindrome(self,head):
		"""
		:type head:ListNode
		:rtype : bool
		"""
		s = []
		while head is not None:
			s.append(head.val)
			head = head.next
		return s == s[::-1]
