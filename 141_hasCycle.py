"""
Linked List Cycle
题目描述：
	Given a linked list, determine if it has a cycle in it.
	Follow up:Can you solve it without using extra space?
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 方法一
class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

# 方法二
class Solution:
	def hasCycle(self,head):
		"""
		:type head:ListNode
		:rtype : bool
		"""
		if head is None or head.next is None:
			return False

		slow = head
		fast = head.next
		while fast and fast.next:
			if slow == fast:
				return True
			slow = slow.next
			fast = fast.next.next
		return False


