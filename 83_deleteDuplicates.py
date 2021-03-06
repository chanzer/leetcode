"""
Remove Duplicates from Sorted List
题目描述：
	Given a sorted linked list, delete all duplicates such
that each element appear only once.

Example 1:
	Input:  1->1->2
	Output: 1->2

Example 2:
	Input:  1->1->2->3->3
	Output: 1->2->3
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self):
        self.val = None
        self.next = None

class Solution:
	def deleteDuplicates(self,head):
		"""
		:type head:ListNode
		:rtype :ListNode
		"""
        cur = head
        while cur:
            while cur.next and cur.val == cur.next.val:
            	 # skip duplicated node
                cur.next = cur.next.next
            # not duplicate of current node, move to next node
            cur = cur.next
        return head
