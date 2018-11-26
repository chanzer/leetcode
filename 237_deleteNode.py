"""
Delete Node in a Linked List
题目描述：
	Write a function to delete a node (except the tail) in a
singly linked list, given only access to that node.
	Given linked list -- head = [4,5,1,9], which looks like
following:4 -> 5 -> 1 -> 9


Example 1:
	Input:  head = [4,5,1,9], node = 5
	Output: [4,1,9]

Example 2:
	Input:  head = [4,5,1,9], node = 1
	Output: [4,5,9]
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def deleteNode(self,node):
		"""
		:type node:ListNode
		:rtype : void do not return anything,modify node in-place
		"""
		node.val = node.next.val
		node.next = node.next.next
